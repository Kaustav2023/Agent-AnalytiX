# 🤖 Agent-AnalytiX Research Analyst Multi-Agent AI System
 
An **AI-powered research system** that uses a team of intelligent agents to perform deep, real-time market research and strategic analysis — all within a sleek Streamlit dashboard.

---

## 🧠 Overview

The **Multi-Agent Research Analyst** automates the entire market research workflow.  
It performs **real-time web research**, **insight summarization**, **strategic reasoning**, and **report generation** using a coordinated set of specialized AI agents.

Designed for founders, analysts, and strategists who want **fast, structured, and data-driven market intelligence**.

---

## 🎯 Features

- 🔍 **Real-time Web Research** — Gathers the latest data using the [Serper.dev](https://serper.dev) search API  
- 🧩 **Multi-Agent Collaboration** — Four specialized AI agents communicate and reason together  
- 🧠 **Strategic Analysis** — Performs SWOT, competitor comparisons, and strategic recommendations  
- 📊 **Executive Dashboard** — Interactive and elegant interface built with Streamlit  
- 📝 **Export Reports** — One-click export of insights as a Markdown report  

---

## 🤖 The Agent Team

| Agent | Role | Description |
|-------|------|-------------|
| 🧑‍💻 **Researcher** | Data Collector | Searches the web for relevant information and sources |
| 🧾 **Summarizer** | Insight Distiller | Extracts and summarizes key findings |
| 🧠 **Strategist** | Analyst | Conducts SWOT and competitive analysis, generating recommendations |
| 🎤 **Presenter** | Report Builder | Formats and presents insights in structured Markdown reports |

---

## 🧱 Tech Stack

- ⚙️ **CrewAI** – Multi-agent orchestration  
- 🪄 **LangChain** – LLM integration and tool coordination  
- ⚡ **Groq** – Ultra-fast LLM inference  
- 🌐 **Serper** – Real-time Google search results  
- 🖥️ **Streamlit** – Interactive dashboard UI  

---

## 🚀 Quick Start

### 1️⃣ Create and navigate to the project folder

mkdir Multi-Agent-Research-Analyst
cd Multi-Agent-Research-Analyst

### 2️⃣ Create a virtual environment
python -m venv .venv
.venv\Scripts\activate     # (Windows)
# or
source .venv/bin/activate  # (macOS/Linux)

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Set up environment variables

Create a .env file in the project root and add your API keys:

SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key

### 5️⃣ Run the Streamlit dashboard
streamlit run app.py

💡 Usage Guide

Open your browser at http://localhost:8501

Enter your research topic in the input field

Click Start Analysis

Watch as the agents collaborate in real time

Review results and download the Markdown report

📂 Project Structure  
📁 Multi-Agent-Research-Analyst  
│  
├── app.py                 # Main Streamlit dashboard  
├── agent.py               # Agent logic  
├── tools.py               # Helper functions and configuration 
├── task.py                # Task definitions  
├── crew.py                # Main Agent Orchestration  
├── requirements.txt       # Project dependencies   
├── .env                   # API keys (not committed)   
└── README.md              # Project documentation  

🧩 Example Output

Input: "Market research on AI-driven CRM tools in 2025"
Output:

Competitive landscape overview

SWOT analysis of top players

Key innovation trends

Recommended strategy summary

Downloadable Markdown report

### 🛠️ Future Enhancements

### 📈 Integration with Notion / Google Docs for direct export

### 🔔 Automated daily or weekly research reports

### 💬 Conversational chat mode between agents and user

### 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo, create a branch, and submit a pull request.
