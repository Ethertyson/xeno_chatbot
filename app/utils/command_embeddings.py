import os
import numpy as np


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

EMBEDDINGS_FILE = os.path.join(
    BASE_DIR,
    "models",
    "xeno_commands.npz",
)


def load_command_embeddings():
    """
    Load pre-generated command embeddings.

    This file is generated once using
    scripts/generate_embeddings.py.

    SentenceTransformer is NOT required here.
    """

    data = np.load(
        EMBEDDINGS_FILE,
        allow_pickle=False,
    )

    topic_commands = data["topic_commands"]
    topic_embeddings = data["topic_embeddings"]

    basic_commands = data["basic_commands"]
    basic_embeddings = data["basic_embeddings"]

    return topic_commands, topic_embeddings, basic_commands, basic_embeddings