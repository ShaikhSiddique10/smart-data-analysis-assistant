# 🤖 Offline Data Analyst Chatbot

A smart, offline, AI-powered chatbot that acts like a human data analyst. Upload your CSV datasets, ask questions, and get Python-generated insights, summaries, and visualizations — all locally, with no internet or OpenAI API needed.

---

## ✅ Features

- Upload any CSV file for instant analysis
- Natural language chat interface with context retention
- Generates Python code, charts, and explanations on the fly
- Provides smart insights and suggestions
- "Show Insights", "Clear Chat", and multi-turn conversation support
- 100% offline and free — runs on your own machine

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Interface:** Streamlit
- **LLM Backend:** Mistral 7B (GGUF format via llama.cpp)
- **Libraries:** Pandas, Matplotlib, Seaborn, llama-cpp-python, Streamlit, NumPy
- **Optional:** Langchain (for future extensions)

---

## ⚙️ Installation

```bash
git clone https://github.com/ShaikhSiddique10/data-analyst-chatbot
cd data-analyst-chatbot
pip install -r requirements.txt
```

## 🚀 Usage
1. Start the Chatbot Locally
streamlit run app.py

##  Upload Dataset
Upload a CSV file via the web interface and start asking questions like:

"What is the average revenue by category?"

"Show me a bar chart of sales by region"

"Find trends in this dataset"

"Which column has the most missing data?


## 📊 Results / Capabilities
Summarizes dataset shape, columns, datatypes, and missing values

Automatically suggests and explains visualizations

Finds top-level insights like best/worst performing regions

Generates readable Python code and explanations for all actions

Customizable context length and LLM model support (via llama.cpp)

## 👤 Author Info
Siddique Shaikh 

📧 siddiqueshaikh009@gmail.com

🔗 https://in.linkedin.com/in/siddique-shaikh-23a776265

💻 https://github.com/ShaikhSiddique10

