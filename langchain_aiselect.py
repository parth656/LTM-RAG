import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,TextLoader,Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DATA_DIR = "data"
CHROMA_DIR = "chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
QA_MODEL="deepset/roberta-base-squad2"

TOP_K=3 # top 3 chunks to retrieve for each query
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

documents=[]
documents+=DirectoryLoader(DATA_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader).load()
documents+=DirectoryLoader(DATA_DIR, glob="**/*.docx", loader_cls=Docx2txtLoader).load() 
documents+=DirectoryLoader(DATA_DIR, glob="**/*.txt", loader_cls=TextLoader,loader_kwargs={"encoding": "utf-8"}).load()     
print(f"Loaded Documents/pages: {len(documents)}")    

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks =text_splitter.split_documents(documents)    
embedding_model=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)    
print(f"Created Chunks: {len(chunks)}")

if Path(CHROMA_DIR).exists():
    print("Loading Existing Chroma DB")
    vector_db=Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=EMBEDDING_MODEL,
    )
else:
    print("Creating New Chroma DB")
    vector_db=Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DIR,
    )
    
retriever=vector_db.as_retriever(search_kwargs={"k": TOP_K})
client=InferenceClient(token=HF_TOKEN)
while True:
    question=input("Question: ").strip()
    if question.lower() in ["exit","quit"]:
        print("Stopped.")
        break
    
    retrieved_docs=retriever.invoke(question)
    context="\n\n".join(doc.page_content for doc  in retrieved_docs)
    answer=client.question_answering(model=QA_MODEL,question=question,context=context,max_answer_len=150)
    answer_text=answer.get("answer",answer) if isinstance(answer,dict) else getattr(answer,"answer",answer)
    print("\n ", answer_text)
    print("\n Sources used")
    
    for i,doc in enumerate(retrieved_docs,start=1):
        source=doc.metadata.get("source","unknown source")
        page=doc.metadata.get("page","")
        print(f"{i}. {source} page {page}")
    
    print("-" *60)