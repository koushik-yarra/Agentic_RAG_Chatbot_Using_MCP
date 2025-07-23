import streamlit as st
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

st.set_page_config(page_title="📚 Agentic RAG Chatbot", layout="wide")
st.title("Agentic RAG chatbot for Multi-Format Document QA Using MCP")

uploaded_files = st.file_uploader(
    "Upload documents (PDF, PPTX, DOCX, TXT, CSV)", 
    type=["pdf", "pptx", "docx", "txt", "csv"], 
    accept_multiple_files=True
)

if "docs" not in st.session_state:
    st.session_state.docs = []
    st.session_state.chunks = []
    st.session_state.chat_history = []

if uploaded_files:
    st.session_state.docs = uploaded_files

if st.button("Submit and Process Documents") and st.session_state.docs:
    with st.spinner("Parsing and processing documents..."):
        ingestion = IngestionAgent()
        st.session_state.chunks = ingestion.parse_and_preprocess(st.session_state.docs)
        st.success("Documents processed successfully!")

st.markdown("---")

query = st.text_input("Ask a question from the uploaded documents")

if st.button("Ask Question") and query and st.session_state.chunks:
    with st.spinner("Getting answer..."):
        retrieval = RetrievalAgent()
        mcp_context = retrieval.get_relevant_chunks(st.session_state.chunks, query)

        llm = LLMResponseAgent()
        mcp_response = llm.generate_response(mcp_context, chat_history=st.session_state.chat_history)

        # Maintain multi-turn conversation
        st.session_state.chat_history.append({"role": "user", "content": query})
        st.session_state.chat_history.append({"role": "assistant", "content": mcp_response["payload"]["answer"]})

        st.subheader("📢 Answer:")
        st.write(mcp_response["payload"]["answer"])

        st.subheader("📌 Source Chunks:")
        for chunk in mcp_response["payload"]["source_chunks"]:
            st.markdown(f"- {chunk}")