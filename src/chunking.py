from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunker:
    def __init__(self):
        pass
    def recursiveoverlap(self,documents):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks =text_splitter.split_documents(documents)  
        
        print("Chunking created")
        return chunks
        
    
    def semantic(self,documents):
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            text_splitter = SemanticChunker(
                embeddings=embeddings,
            breakpoint_threshold_type ="percentile"
            )

            chunks = text_splitter.split_documents(documents)
            print("Semantic Chunks Created")
            return chunks

