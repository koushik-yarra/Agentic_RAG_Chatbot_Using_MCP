from vector_store.faiss_store import FAISSVectorStore
from mcp.mcp_message import create_mcp_message

class RetrievalAgent:
    def __init__(self):
        self.vdb = FAISSVectorStore()

    def get_relevant_chunks(self, chunks, query):
        self.vdb.build_index(chunks)
        top_chunks = self.vdb.search(query)
        return create_mcp_message(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            type_="RETRIEVAL_RESULT",
            payload={"retrieved_context": top_chunks, "query": query}
        )
