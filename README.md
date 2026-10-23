# LTM-RAG — Document Question Answering

LTM-RAG is a retrieval-augmented generation project. The dependency manifest includes LangChain packages, Hugging Face embeddings, Chroma, PDF and DOCX loaders, dotenv support, and Google's GenAI SDK.

## Architecture

```text
PDF / DOCX / text files
        -> Loaders
        -> Text splitting
        -> Hugging Face embeddings
        -> Chroma vector store
        -> Retriever
        -> Gemini-backed answer generation
```

This diagram summarizes the intended RAG workflow; confirm the exact implementation and selected models in the source before relying on any specific configuration.

## Technology

- Python
- LangChain and community integrations
- Hugging Face sentence-transformer embeddings
- Chroma vector store
- PDF and DOCX document loaders
- Google GenAI integration
- python-dotenv for local configuration

## Setup

```bash
git clone https://github.com/parth656/LTM-RAG.git
cd LTM-RAG
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Configure the model provider credentials expected by the code using environment variables or a local `.env` file. Never commit real API keys.

## Usage

Inspect the repository for the ingestion and query entry points. Run the ingestion workflow to build or update the index, then run the query application. Exact commands depend on the current source filenames and should be added here after verification.

## Evaluation

Use a repeatable question set with known source passages. Measure retrieval relevance, answer faithfulness, ability to abstain when the corpus lacks an answer, latency, and model usage/cost. Include source citations in answers where supported.

## Security and limitations

- Treat documents as untrusted input; retrieved content must not override system instructions.
- Avoid indexing confidential data without permission.
- Document index persistence and how to rebuild or delete stored vectors.
- LLM answers may be incorrect; verify important claims against the cited source material.

## Release checklist

- [ ] Add exact ingestion/query commands.
- [ ] Document the embedding model and chunking configuration.
- [ ] Add screenshots and example questions.
- [ ] Add tests for loaders, chunking, retrieval, and error handling.
- [ ] Pin dependency versions for reproducible deployment.
