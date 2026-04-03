# Local RAG AI Agent: Pizza Restaurant Assistant 🍕🤖

This project is a completely local, privacy-first AI assistant built using **LangChain**, **Ollama**, and **ChromaDB**. It uses **Retrieval-Augmented Generation (RAG)** to answer user questions about a fictional pizza restaurant by reading through a dataset of realistic customer reviews.

Because the models run locally via Ollama, there are **zero API costs**, **no rate limits**, and **complete data privacy**.

## 🌟 Features
- **100% Local Execution:** Powered by Ollama.
- **RAG Architecture:** The AI doesn't guess; it searches your actual CSV data for context before answering.
- **Vector Database:** Uses ChromaDB and local embeddings to perform semantic searches over restaurant reviews.
- **Educational:** The codebase is heavily commented with the theory and concepts behind Agentic AI and RAG to help beginners understand *how* it works.

## 📋 Prerequisites

Before you can run this project, you need to install [Ollama](https://ollama.com/) on your machine and pull the required models.

Open your terminal and run:
```bash
# Pull the LLM used for answering questions
ollama pull llama3.2

# Pull the embedding model used for the vector database
ollama pull mxbai-embed-large
```

*You will also need Python 3.10+ installed on your system.*

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Naman21nv/Localrunning_AI_agent_python.git
   cd Localrunning_AI_agent_python
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install langchain-ollama langchain-core langchain-chroma chromadb pandas
   ```

## 💻 Usage

### Step 1: Build the Vector Database
Before asking the AI questions, you need to convert the CSV reviews into vector embeddings. 
```bash
python vector.py
```
*Note: This script has built-in logic to check if the database already exists. It will only run the computationally heavy embedding process once, saving the results to a local `./chroma_db` folder.*

### Step 2: Chat with the Agent
Once the database is built, start the interactive chat loop!
```bash
python main.py
```