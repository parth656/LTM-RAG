# LTM-RAG Architecture

This document outlines the RAG flow suggested by the repository's dependency manifest and README. Confirm exact modules, model identifiers, and persistence behavior in source code.

## Ingestion flow

```text
PDF / DOCX / text sources
        -> document loaders
        -> normalized document objects + metadata
        -> recursive text splitting
        -> Hugging Face embeddings
        -> Chroma vector collection
```

## Query flow

```text
User question
    -> embed / retrieve relevant chunks
    -> assemble context
    -> call configured Gemini model
    -> return answer (and source metadata where implemented)
```

## Core responsibilities

- **Loaders:** extract text from supported document formats.
- **Chunking:** create bounded passages with overlap and metadata.
- **Embeddings:** map passages and queries into a shared vector space.
- **Vector store:** persist and search the document index.
- **Generation:** answer using retrieved context.
- **Configuration:** keep API credentials outside source control.

## Evaluation

Create a small golden set of questions linked to source passages. Measure retrieval relevance independently from answer quality. Include unanswerable questions, conflicting passages, long documents, and malformed files. Track latency and token usage if available.

## Operational considerations

- Rebuild the index when source documents or embedding models change.
- Record the embedding model and chunking configuration alongside the index.
- Treat retrieved documents as untrusted content; do not allow them to override system instructions.
- Avoid indexing private documents without authorization.
- Return source citations where supported and make uncertainty visible.
