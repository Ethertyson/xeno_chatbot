import os

import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer
from app.utils.logger import logger


class EmbeddingService:
    """
    Lightweight sentence embedding service using:

        tokenizer
            ↓
        MiniLM ONNX
            ↓
        mean pooling
            ↓
        L2 normalization

    This replaces SentenceTransformer for production inference.

    Expected embedding size for all-MiniLM-L6-v2:

        (384,)
    """

    def __init__(self):
        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )

        model_dir = os.path.join(
            base_dir,
            "models",
            "all-MiniLM-L6-v2",
        )

        model_path = os.path.join(
            model_dir,
            "model.onnx",
        )

        tokenizer_path = os.path.join(
            model_dir,
            "tokenizer.json",
        )

        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"ONNX model not found: {model_path}"
            )

        if not os.path.exists(tokenizer_path):
            raise FileNotFoundError(
                f"Tokenizer not found: {tokenizer_path}"
            )

        # --------------------------------------------------
        # Load tokenizer
        # --------------------------------------------------

        self.tokenizer = Tokenizer.from_file(
            tokenizer_path
        )

        # --------------------------------------------------
        # Configure ONNX Runtime
        # --------------------------------------------------

        session_options = ort.SessionOptions()

        # CPU only.
        #
        # This is what we want for the Railway deployment.
        self.session = ort.InferenceSession(
            model_path,
            sess_options=session_options,
            providers=[
                "CPUExecutionProvider"
            ],
        )

        # --------------------------------------------------
        # Read model input/output information
        # --------------------------------------------------

        self.input_names = {
            input_.name
            for input_ in self.session.get_inputs()
        }

        self.output_names = [
            output.name
            for output in self.session.get_outputs()
        ]

        logger.info(
            "ONNX input names: %s",
            self.input_names,
        )

        logger.info(
            "ONNX output names: %s",
            self.output_names,
        )

    def _tokenize(self, text: str):
        """
        Tokenize a single sentence.

        Returns:
            input_ids
            attention_mask
            token_type_ids
        """

        self.tokenizer.enable_truncation(
            max_length=128
        )

        self.tokenizer.enable_padding(
            length=128,
            pad_id=0,
            pad_token="[PAD]",
        )

        encoded = self.tokenizer.encode(
            text
        )

        input_ids = np.array(
            [encoded.ids],
            dtype=np.int64,
        )

        attention_mask = np.array(
            [encoded.attention_mask],
            dtype=np.int64,
        )

        token_type_ids = np.array(
            [encoded.type_ids],
            dtype=np.int64,
        )

        return (
            input_ids,
            attention_mask,
            token_type_ids,
        )

    def _mean_pooling(
        self,
        token_embeddings: np.ndarray,
        attention_mask: np.ndarray,
    ):
        """
        Mean-pool token embeddings using the
        attention mask.

        token_embeddings:

            (batch_size, sequence_length, hidden_size)

        attention_mask:

            (batch_size, sequence_length)
        """

        mask = attention_mask[
            ..., None
        ].astype(
            np.float32
        )

        masked_embeddings = (
            token_embeddings * mask
        )

        summed_embeddings = (
            masked_embeddings.sum(
                axis=1
            )
        )

        token_count = np.clip(
            mask.sum(axis=1),
            a_min=1e-9,
            a_max=None,
        )

        return (
            summed_embeddings
            / token_count
        )

    def _normalize(
        self,
        embeddings: np.ndarray,
    ):
        """
        L2-normalize embeddings.

        After normalization, cosine similarity
        can be calculated using a simple dot product.
        """

        norms = np.linalg.norm(
            embeddings,
            axis=1,
            keepdims=True,
        )

        norms = np.clip(
            norms,
            a_min=1e-12,
            a_max=None,
        )

        return (
            embeddings / norms
        )

    def encode(
        self,
        text: str,
    ) -> np.ndarray:
        """
        Generate an embedding for one user query.

        Args:
            text:
                User input string.

        Returns:
            numpy.ndarray

            Shape:
                (384,)

            dtype:
                float32
        """

        if not isinstance(
            text,
            str,
        ):
            raise TypeError(
                "text must be a string"
            )

        text = text.strip()

        if not text:
            raise ValueError(
                "text cannot be empty"
            )

        (
            input_ids,
            attention_mask,
            token_type_ids,
        ) = self._tokenize(text)

        # --------------------------------------------------
        # Prepare ONNX inputs
        # --------------------------------------------------

        inputs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
        }

        # Some BERT/MiniLM ONNX exports include
        # token_type_ids while others don't.
        if (
            "token_type_ids"
            in self.input_names
        ):
            inputs[
                "token_type_ids"
            ] = token_type_ids

        # --------------------------------------------------
        # Run ONNX inference
        # --------------------------------------------------

        outputs = self.session.run(
            None,
            inputs,
        )

        # The MiniLM ONNX model's first output
        # contains token-level embeddings.
        token_embeddings = outputs[0]

        # --------------------------------------------------
        # Mean pooling
        # --------------------------------------------------

        sentence_embedding = (
            self._mean_pooling(
                token_embeddings,
                attention_mask,
            )
        )

        # --------------------------------------------------
        # L2 normalization
        # --------------------------------------------------

        sentence_embedding = (
            self._normalize(
                sentence_embedding
            )
        )

        # Remove batch dimension.
        sentence_embedding = (
            sentence_embedding[0]
        )

        return sentence_embedding.astype(
            np.float32
        )