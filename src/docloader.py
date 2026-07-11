from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,TextLoader,Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class MainLoader:
    def __init__(self):
        pass
    def allfileLoader(self):
        DATA_DIR = "data"
        documents=[]
        documents+=DirectoryLoader(DATA_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader).load()
        documents+=DirectoryLoader(DATA_DIR, glob="**/*.docx", loader_cls=Docx2txtLoader).load() 
        documents+=DirectoryLoader(DATA_DIR, glob="**/*.txt", loader_cls=TextLoader,loader_kwargs={"encoding": "utf-8"}).load()     
        print(f"Loaded Documents/pages: {len(documents)}")  
        return documents