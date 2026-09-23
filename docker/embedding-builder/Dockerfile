FROM python:3.11-slim

WORKDIR /build

COPY requirements-embedding.txt ./

RUN pip install --no-cache-dir -r requirements-embedding.txt

COPY scripts/embedding_builder/ ./

RUN mkdir -p /build/models

CMD ["python", "build_command_embeddings.py"]