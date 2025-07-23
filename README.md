# 🤖 Agentic RAG Chatbot for Multi-Format Document QA using Model Context Protocol (MCP)

An AI-powered multi-turn document QA chatbot that supports PDF, DOCX, PPTX, CSV, and TXT files. It uses **LangChain**, **Google Gemini**, **FAISS**, and **MCP (Model Context Protocol)** to orchestrate three agents: **Ingestion**, **Retrieval**, and **LLM Response**.

---

## 📁 Project Structure

```
.
├── app.py                      # Streamlit app entry point
├── requirements.txt            # Python dependencies
├── agents/
│   ├── ingestion_agent.py      # Handles document parsing and chunking
│   ├── retrieval_agent.py      # Retrieves relevant chunks using FAISS
│   └── llm_response_agent.py   # Generates answers using Gemini LLM
├── vector_store/
│   └── faiss_store.py          # FAISS-based vector store for semantic search
├── mcp/
│   └── mcp_message.py          # Model Context Protocol message utilities
└── README.md
```

## 🚀 Features

- **Multi-turn Chat**: Maintains chat history for context-aware answers.
- **Document Support**: Handles PDF, DOCX, PPTX, CSV, and TXT files.
- **Semantic Search**: Uses FAISS and Sentence Transformers for retrieval.
- **LLM Integration**: Uses Google Gemini via LangChain for answer generation.
- **Agentic Orchestration**: Modular agents for ingestion, retrieval, and response.

## 🛠️ Setup


1. **Clone the repository**  
   ```sh
   git clone <repo-url>
   cd <project-folder>
   ```

2. **Create a virtual environment**  
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
   *(On macOS/Linux, use `source venv/bin/activate` instead of the last line above)*

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

5. **Run the app**  
   ```sh
   streamlit run app.py
   ```

## 🧩 How It Works

1. **Ingestion Agent**: Parses and preprocesses uploaded documents, splitting them into text chunks.
2. **Retrieval Agent**: Builds a FAISS index and retrieves the most relevant chunks for a user query.
3. **LLM Response Agent**: Uses Gemini LLM to generate a response based on the retrieved context and maintains chat history.

## 📄 Supported File Types

- PDF (`.pdf`)
- Word (`.docx`)
- PowerPoint (`.pptx`)
- CSV (`.csv`)
- Text (`.txt`)

## 📚 Dependencies

See `requirements.txt` for all dependencies, including:
- streamlit
- langchain
- langchain-google-genai
- google-generativeai
- faiss-cpu
- sentence-transformers
- python-docx
- python-pptx
- PyMuPDF
- pandas
- pytesseract
- Pillow

## 📝 License

koushikyerra3@gmail.com
---

Feel free to further customize this `README.md` for your needs!
