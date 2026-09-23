# Xeno Version 2 – Lightweight AI Style Chatbot

Backend-focused full-stack chatbot application built with **Python, Flask, semantic search, ONNX Runtime, and a lightweight NLP pipeline**.

Xeno V2 focuses on reducing production memory usage while preserving the existing chatbot functionality and semantic command-matching behavior.

---

## 🚀 Overview

Xeno is an AI-style chatbot capable of understanding natural-language commands and mapping them to predefined responses.

The project originally used `SentenceTransformer` and PyTorch for semantic command matching. In **Xeno V2**, the production inference pipeline was redesigned using:

- **ONNX Runtime**
- **MiniLM (`all-MiniLM-L6-v2`)**
- **Hugging Face Tokenizers**
- **NumPy**
- **Precomputed command embeddings**
- **NumPy cosine-similarity search**

This significantly reduces the memory footprint of the production application.

---

## ✨ Features

- 🤖 Smart natural-language input parsing
- 🧠 Semantic command matching
- 🔎 Lightweight semantic search
- ⚡ ONNX-based sentence embedding generation
- 📦 Precomputed command embeddings
- 🧮 Mathematical expression evaluation
- 🔢 Number and operator recognition
- ⚙️ Bitwise operations
- 🕐 Timezone-aware date and time responses
- 🌐 News search integration
- 💬 Basic assistant/chatbot responses
- 🧩 Expandable command dictionary
- 🐳 Docker support
- 🚂 Railway deployment support
- 📊 Memory and performance monitoring
- 📴 Offline semantic command matching
- 🛠️ Dedicated embedding-builder utility

---

## 🧠 Xeno V2 – Resource Optimization

The main goal of V2 was to reduce the memory consumption of the semantic-matching system.

### V1

The original implementation loaded:

```text
SentenceTransformer
        ↓
PyTorch
        ↓
all-MiniLM-L6-v2
        ↓
Generate embeddings for all commands at startup
```

This resulted in approximately:

```text
~804 MB RSS
```

during application initialization.

### V2

The production implementation now uses:

```text
User Query
    ↓
Tokenizer
    ↓
ONNX Runtime
    ↓
MiniLM Embedding
    ↓
NumPy Cosine Similarity
    ↓
Precomputed Command Embeddings
    ↓
Best Matching Command
```

Production startup memory was reduced to approximately:

```text
~202 MB RSS
```

This represents approximately a **75% reduction in observed startup memory usage** compared with the previous implementation.

---

## 🔍 Semantic Search Architecture

Xeno contains approximately **1,522 predefined semantic commands**:

```text
Topic Commands : 1,036
Basic Commands :   486
-----------------------
Total           : 1,522
```

Instead of generating embeddings for all commands every time the application starts, the embeddings are generated once and stored as a NumPy `.npz` file.

### Production flow

```text
User Input
    │
    ▼
Tokenizer
    │
    ▼
ONNX Runtime
    │
    ▼
Query Embedding
    │
    ▼
NumPy Similarity Search
    │
    ▼
Precomputed Command Embeddings
    │
    ▼
Best Matching Command
    │
    ▼
Chatbot Response
```

The stored embeddings use:

```text
Model       : all-MiniLM-L6-v2
Dimensions  : 384
Data Type   : float32
Similarity  : Cosine Similarity
Storage     : NumPy NPZ
```

The embeddings are normalized before storage, allowing cosine similarity to be calculated efficiently using a dot product.

---

## 📦 Precomputed Command Embeddings

The generated embedding file is:

```text
models/xeno_commands.npz
```

It contains:

```text
topic_commands
topic_embeddings

basic_commands
basic_embeddings
```

Expected shapes:

```text
Topic Commands      : (1036,)
Topic Embeddings    : (1036, 384)

Basic Commands      : (486,)
Basic Embeddings    : (486, 384)
```

The generated file is approximately **2.1 MB**, making it significantly smaller and more deployment-friendly than generating and storing embeddings dynamically at application startup.

---

## 🛠️ Embedding Builder

Embedding generation is separated from the production application.

The embedding builder is a dedicated Docker utility that uses `SentenceTransformer` only during the offline embedding-generation process.

Production does **not** load SentenceTransformer or PyTorch.

### Builder architecture

```text
Command Dictionary
        │
        ▼
SentenceTransformer
        │
        ▼
all-MiniLM-L6-v2
        │
        ▼
Normalized Embeddings
        │
        ▼
xeno_commands.npz
```

The builder is located at:

```text
scripts/embedding_builder/
```

and uses:

```text
docker/embedding-builder/Dockerfile
```

Builder dependencies are kept separate from the production requirements.

---

## 🧰 Tech Stack

### Backend

- Python
- Flask
- REST API
- Object-Oriented Programming

### AI / NLP

- ONNX Runtime
- Hugging Face Tokenizers
- `all-MiniLM-L6-v2`
- NumPy
- Semantic Search
- Sentence Embeddings

### Utilities

- NumExpr
- Word2Number
- pytz
- psutil

### Frontend

- HTML
- CSS
- JavaScript

### Database / Backend Infrastructure

- SQLAlchemy

### Deployment

- Docker
- Railway

---

## 📁 Project Structure

```text
xeno_chatbot/
│
├── app/
│   │
│   ├── models/
│   │   └── chatBot.py
│   │
│   ├── routes/
│   │
│   ├── static/
│   │
│   ├── templates/
│   │
│   ├── utils/
│   │   ├── embedding_service.py
│   │   ├── command_embeddings.py
│   │   ├── semantic_search.py
│   │   └── memory_utils.py
│   │
│   └── __init__.py
│
├── models/
│   └── xeno_commands.npz
│   │
│   └── all-MiniLM-L6-v2/
│           ├── model.onnx
│           └── tokenizer.json
│
├── scripts/
│   └── embedding_builder/
│       ├── build_command_embeddings.py
│       └── commands.py
│
├── docker/
│   └── embedding-builder/
│       └── Dockerfile
│
├── run.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-embedding.txt
└── .dockerignore
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ethertyson/xeno_chatbot.git
cd xeno_chatbot
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create/configure the required environment variables.

Example:

```env
FLASK_ENV=development

GOOGLE_NEWS_API_KEY=your_key
GOOGLE_NEWS_API_HOST=google_news_api_host
```

Add any other environment-specific configuration required by the application.

---

## ▶️ Run the Application

You can start the Flask application using:

```bash
python run.py
```

or:

```bash
flask run
```

The application will be available on:

```text
http://localhost:5000
```

---

## 🐳 Docker

### Build the application image

```bash
docker build -t xeno-chatbot .
```

### Run the application

```bash
docker run -p 5000:5000 xeno-chatbot
```

---

## 🧪 Docker Compose

The project also includes Docker Compose configuration for local development.

Start the application:

```bash
docker compose up xeno
```

---

## 🔨 Regenerating Command Embeddings

The production application does not generate command embeddings during startup.

If `models/xeno_commands.npz` needs to be regenerated, use the dedicated embedding-builder service.

Run:

```bash
docker compose run embedding-builder
```

The generated file will be created at:

```text
models/xeno_commands.npz
```

After generating the file, start the application normally:

```bash
docker compose up xeno
```

### Important

The embedding builder is a **development/build utility only**.

It is not required to run the production application after `xeno_commands.npz` has been generated.

---

## 🔌 API

### Chat API

#### Endpoint

```text
POST /chatAiModel
```

#### Example Request

```json
{
    "message": "how do i create a table in mysql"
}
```

#### Example Response

```json
{
    "response": "CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    PRIMARY KEY (column1)
);"
}
```

The exact response depends on the command dictionary and semantic similarity result.

---

## 🧮 Mathematical Operations

Xeno also supports mathematical and expression-based queries.

Examples include:

```text
10 + 20
5 * 8
100 / 4
2 ^ 5
10 & 3
20 | 5
```

The application contains dedicated handling for:

- Number-based calculations
- Mathematical expressions
- Operators
- Bitwise operations

---

## 🌐 News and Date/Time Features

Xeno supports special command handling for:

- News queries
- Current time
- Current date
- Timezone-aware responses

These commands are handled separately from the standard semantic command matching flow where required.

---

## 📊 Performance Monitoring

During development and deployment testing, Xeno includes memory and execution-time logging.

The application tracks:

- Application startup memory
- Model initialization memory
- Command embedding loading
- Query embedding execution time
- Semantic search execution time
- Runtime memory usage

Example:

```text
[MEMORY] ...
```

This instrumentation was used to compare the V1 and V2 resource footprint.

---

## 🚂 Railway Deployment

Xeno is designed to be deployable using Docker on Railway.

The production deployment uses the root:

```text
Dockerfile
```

The production application does not run the embedding-builder service.

The required production artifacts are already included in the repository:

```text
app/models/all-MiniLM-L6-v2/model.onnx
app/models/all-MiniLM-L6-v2/tokenizer.json
models/xeno_commands.npz
```

Therefore, Railway can start the application directly without running the embedding-generation process.

---

## 🔄 V1 → V2 Changes

### Removed from Production

The production application no longer requires:

```text
SentenceTransformer
PyTorch
Transformers
Scikit-learn
SciPy
```

for semantic command inference.

### Added

```text
ONNX Runtime
Hugging Face Tokenizers
NumPy-based similarity search
Precomputed command embeddings
Dedicated embedding-builder service
```

### Architecture Change

#### V1

```text
Application Startup
      │
      ▼
Load SentenceTransformer
      │
      ▼
Load PyTorch
      │
      ▼
Generate 1,522 embeddings
      │
      ▼
Start Application
```

#### V2

```text
Build Time
    │
    ▼
Generate command embeddings once
    │
    ▼
Store xeno_commands.npz
    │
    │
    ▼
Production Startup
    │
    ▼
Load ONNX Model
    │
    ▼
Load Precomputed Embeddings
    │
    ▼
Ready
```

---

## 📈 V1 vs V2

| Area | V1 | V2 |
|---|---|---|
| Embedding Model | SentenceTransformer | ONNX Runtime |
| Model | all-MiniLM-L6-v2 | all-MiniLM-L6-v2 |
| PyTorch | Required | Removed from production |
| Transformers | Required | Removed from production |
| Command Embeddings | Generated at startup | Precomputed |
| Stored Embeddings | No | `.npz` |
| Similarity Search | SentenceTransformer utility | NumPy |
| Production Inference | Heavy ML stack | Lightweight ONNX |
| Command Count | 1,522 | 1,522 |
| Embedding Dimension | 384 | 384 |
| Observed Startup RSS | ~804 MB | ~202 MB |
| Embedding Builder | Part of application flow | Separate Docker utility |

---

## 💡 Design Decisions

### Why precompute embeddings?

The command dictionary changes much less frequently than user queries.

Generating embeddings for all commands every time the application starts is unnecessary overhead.

Instead:

```text
Commands
   ↓
Generate embeddings once
   ↓
Store embeddings
   ↓
Load during application startup
```

Only the incoming user query requires embedding generation at runtime.

---

### Why ONNX Runtime?

ONNX Runtime allows the MiniLM model to run without loading the complete PyTorch/SentenceTransformers stack into the production application.

This significantly reduces the production memory footprint while retaining the same underlying embedding model.

---

### Why NumPy?

Only around 1,522 command embeddings are stored.

For this dataset size, a simple NumPy similarity search is sufficient and avoids introducing a separate vector database or external service.

---

### Why not use a vector database?

The current command dataset is small enough that introducing a vector database would add unnecessary:

- Infrastructure
- Memory usage
- Network overhead
- Deployment complexity

The embeddings can comfortably be stored and searched locally using NumPy.

---

## 🔒 Offline Capability

After the required model files and precomputed embeddings are present, semantic command matching can run locally without requiring an external vector database or online embedding API.

Required model files:

```text
app/models/all-MiniLM-L6-v2/model.onnx
app/models/all-MiniLM-L6-v2/tokenizer.json
```

Required command embeddings:

```text
models/xeno_commands.npz
```

---

## 🧩 Extending the Command Dictionary

New commands can be added to the command dictionaries used by Xeno.

When command keys are changed or added, regenerate the precomputed embeddings:

```bash
docker compose run embedding-builder
```

This updates:

```text
models/xeno_commands.npz
```

Commit the regenerated file together with the command-dictionary changes.

---

## 🧪 Testing

After starting the application, test the chatbot using natural-language variations of supported commands.

Examples:

```text
What is a database?
How do I create a table in mysql?
What command creates a table in MySQL?
What is the current time?
What is today's date?
Calculate 25 * 4
```

Semantic matching allows different phrasings of supported commands to map to the corresponding predefined command.

---

## 🚀 Future Improvements

Potential future improvements include:

- Further memory optimization
- Cleanup of temporary development profiling/logging code
- Improved semantic matching thresholds
- Additional command coverage
- Improved query normalization
- More robust intent classification
- Continuous application availability improvements
- Additional lightweight AI capabilities

---

## 👨‍💻 Author

**Pritanshu Srivastava**

AI Software Engineer | Applied AI Engineer | GenAI | RAG | LLM Systems | Python Backend Developer

- **LinkedIn:** https://www.linkedin.com/in/pritanshu-srivastava-59aaa7226/
- **GitHub:** https://github.com/Ethertyson
- **HackerRank:** https://hackerrank.com/profile/pritanshusrivas1

---

## 📄 License

This project is intended for learning, experimentation, and personal development purposes.

---

## ⭐ Xeno V2

Xeno V2 focuses on keeping the chatbot architecture simple and deployment-friendly while significantly reducing the production memory footprint through:

```text
ONNX Runtime
      +
Precomputed Embeddings
      +
NumPy Similarity Search
      +
Lightweight Flask Backend
```

**From a heavy startup embedding pipeline to a lightweight production semantic-search architecture.**