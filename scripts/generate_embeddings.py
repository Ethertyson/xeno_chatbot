import os
import sys
import numpy as np

from sentence_transformers import SentenceTransformer


# Allow importing the Xeno app package when this script is executed from the project root.
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, BASE_DIR)


from app.utils import commands


MODEL_NAME = "all-MiniLM-L6-v2"

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "models",
)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "xeno_commands.npz",
)


def build_commands():
    """
    Build the same command dictionary currently used by makeReply.py.
    """

    all_topic_commands = {
        **commands.windows_cmds,
        **commands.linux_cmds,
        **commands.macos_cmds,
        **commands.github_cmds,
        **commands.mysql_queries,
        **commands.random_facts,
        **commands.powershell_cmds,
        **commands.cs_concepts,
        **commands.news_queries,
        **commands.time_date_queries,
    }

    initial_commands = {
        **commands.basic_cmds,
        **commands.assistant_role_responses,
        **commands.creator_queries,
        **commands.identity_responses,
        **commands.internet_info,
        **commands.tech_info,
        **commands.common_searches,
        **commands.nature_facts,
        **commands.most_searches,
    }

    return all_topic_commands, initial_commands


def main():

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True,
    )

    topic_commands, basic_commands = build_commands()

    topic_command_keys = list(topic_commands.keys())
    basic_command_keys = list(basic_commands.keys())

    from app.utils.memory_utils import log_memory

    log_memory(
        f"Found {len(topic_command_keys)} topic commands and {len(basic_command_keys)} basic commands."
    )

    log_memory(
        f"Loading model: {MODEL_NAME}"
    )

    model = SentenceTransformer(
        MODEL_NAME
    )

    log_memory("Generating embeddings...")

    topic_embeddings = model.encode(
        topic_command_keys,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    basic_embeddings = model.encode(
        basic_command_keys,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    topic_embeddings = topic_embeddings.astype(
        np.float32
    )

    basic_embeddings = basic_embeddings.astype(
        np.float32
    )

    log_memory(
        f"Topic embedding shape: {topic_embeddings.shape}"
        f"Basic embedding shape: {basic_embeddings.shape}"
    )

    log_memory(
        f"Topic embedding dtype: {topic_embeddings.dtype}"
        f"Basic embedding dtype: {basic_embeddings.dtype}"
    )

    np.savez_compressed(
        OUTPUT_FILE,

        topic_commands=np.array(
            topic_command_keys,
            dtype=str,
        ),

        topic_embeddings=topic_embeddings,

        basic_commands=np.array(
            basic_command_keys,
            dtype=str,
        ),

        basic_embeddings=basic_embeddings,
    )

    log_memory(
        f"Saved embeddings to:\n"
        f"{OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()