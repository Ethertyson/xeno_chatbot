import numpy as np


def find_best_match(
    query_embedding: np.ndarray,
    command_embeddings: np.ndarray,
    commands: np.ndarray,
):
    """
    Find the command with the highest cosine similarity.

    Both query_embedding and command_embeddings are expected
    to be normalized.

    Returns:
        matched_command,
        similarity_score
    """

    scores = command_embeddings @ query_embedding

    best_index = int(
        np.argmax(scores)
    )

    return (
        commands[best_index],
        float(scores[best_index]),
    )