from src.docloader import MainLoader

from src.chunking import Chunker
from src.vectorization import Vectorizer


from src.retriever import   mainRetriever
mn=MainLoader()
ch=Chunker()
vc=Vectorizer()
mnr=mainRetriever()
documents=mn.allfileLoader()
print("test1")
chunked_doc=ch.recursiveoverlap(documents)
print("test2")
vector_db=vc.hfembedder(chunked_doc)
fncontext=mnr.TopKRetriever("What is Google do in latest AI",vector_db,3)
print(fncontext)

