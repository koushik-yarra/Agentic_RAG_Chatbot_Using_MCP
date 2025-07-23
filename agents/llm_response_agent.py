import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from mcp.mcp_message import create_mcp_message
from dotenv import load_dotenv

load_dotenv()

class LLMResponseAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            temperature=0.4,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    def generate_response(self, mcp_context, chat_history=None):
        retrieved = mcp_context["payload"]["retrieved_context"]
        query = mcp_context["payload"]["query"]
        context = "\n\n".join(retrieved)

        prompt = f"""You are a helpful assistant. Use the document context to answer the user's question clearly.

Document Context:
{context}

User Question:
{query}

Answer:
"""

        response = self.llm([HumanMessage(content=prompt)]).content

        return create_mcp_message(
            sender="LLMResponseAgent",
            receiver="UI",
            type_="LLM_RESPONSE",
            payload={"answer": response.strip(), "source_chunks": retrieved}
        )
