
class mainRetriever:
    def __init__(self):
        pass
    def TopKRetriever(self,question,vector_db,TOP_K=3):
        retriever=vector_db.as_retriever(search_kwargs={"k": TOP_K})
        retrieved_docs=retriever.invoke(question)
        context="\n\n".join(doc.page_content for doc  in retrieved_docs)
        return context
