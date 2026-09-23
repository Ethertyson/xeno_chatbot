import os

import numpy as np
from sentence_transformers import SentenceTransformer

import commands


MODEL_NAME = "all-MiniLM-L6-v2"


# Project root
BASE_DIR = "/build"

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "models",
)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "xeno_commands.npz",
)


def build_commands():

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

    print("=" * 60)
    print("Xeno Command Embedding Builder")
    print("=" * 60)

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True,
    )

    # -----------------------------------------------------
    # Build command dictionaries
    # -----------------------------------------------------

    topic_commands, basic_commands = build_commands()

    topic_command_keys = list(
        topic_commands.keys()
    )

    basic_command_keys = list(
        basic_commands.keys()
    )

    print(
        f"\nTopic commands : {len(topic_command_keys)}"
    )

    print(
        f"Basic commands : {len(basic_command_keys)}"
    )

    # -----------------------------------------------------
    # Load model
    # -----------------------------------------------------

    print(
        f"\nLoading model: {MODEL_NAME}"
    )

    model = SentenceTransformer(
        MODEL_NAME
    )

    print(
        "Model loaded."
    )

    # -----------------------------------------------------
    # Generate topic embeddings
    # -----------------------------------------------------

    print(
        "\nGenerating topic command embeddings..."
    )

    topic_embeddings = model.encode(
        topic_command_keys,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    # -----------------------------------------------------
    # Generate basic embeddings
    # -----------------------------------------------------

    print(
        "\nGenerating basic command embeddings..."
    )

    basic_embeddings = model.encode(
        basic_command_keys,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    # -----------------------------------------------------
    # Convert to float32
    # -----------------------------------------------------

    topic_embeddings = topic_embeddings.astype(
        np.float32
    )

    basic_embeddings = basic_embeddings.astype(
        np.float32
    )

    print(
        f"\nTopic embedding shape: "
        f"{topic_embeddings.shape}"
    )

    print(
        f"Basic embedding shape: "
        f"{basic_embeddings.shape}"
    )

    print(
        f"Topic embedding dtype: "
        f"{topic_embeddings.dtype}"
    )

    print(
        f"Basic embedding dtype: "
        f"{basic_embeddings.dtype}"
    )

    # -----------------------------------------------------
    # Save
    # -----------------------------------------------------

    print(
        f"\nSaving embeddings to:"
        f"\n{OUTPUT_FILE}"
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

    # -----------------------------------------------------
    # File information
    # -----------------------------------------------------

    file_size_mb = (
        os.path.getsize(OUTPUT_FILE)
        / (1024 * 1024)
    )

    print(
        "\nEmbedding file created successfully."
    )

    print(
        f"File size: {file_size_mb:.2f} MB"
    )

    print(
        f"Output: {OUTPUT_FILE}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()