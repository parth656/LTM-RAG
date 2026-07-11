from src.docloader import MainLoader
from src.chunking import Chunker
from src.vectorization import Vectorizer
from src.retriever import mainRetriever

mnr = mainRetriever()
mnl = MainLoader()
ch = Chunker()
vc = Vectorizer()

documents = mnl.allfileLoader()
print("test1")
chunked_doc = ch.semantic(documents)
print("test2")
vector_db = vc.hfembedder(chunked_doc)


fncontext = mnr.TopKRetriever("Who is CEO of Anthropic",vector_db,3)
print(fncontext)