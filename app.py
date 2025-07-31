import streamlit as st
import pandas as pd
from analyzer import summarize_data, top_insight
from visualizer import (
    plot_bar, plot_line, plot_scatter, plot_pie, plot_heatmap
)
from llm import ask_local_llm  

st.set_page_config(page_title="AI-Powered Data Analyst", layout="wide")
st.title("📊 Smart Data Analyst Dashboard")


st.sidebar.header("📁 Upload Your CSV File")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🧾 Data Preview")
    st.dataframe(df.head())


    st.subheader("📋 Data Summary")
    if st.checkbox("Show Summary"):
        summary = summarize_data(df)
        st.markdown(f"**Shape:** {summary['shape']}")
        st.markdown(f"**Columns:** {', '.join(summary['columns'])}")
        st.markdown("**Missing Values:**")
        st.json({k: v for k, v in summary['missing'].items() if v > 0})
        st.markdown("**Data Types:**")
        st.json(summary['dtypes'])
        st.markdown("**Statistical Summary:**")
        st.dataframe(pd.DataFrame(summary['summary']))

    st.subheader("💡 Auto Insights")
    if st.button("🔍 Show Insight"):
        insight = top_insight(df)
        st.success(insight)

    st.subheader("📊 Create Visualization")
    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line", "Scatter", "Pie", "Heatmap"])
    if chart_type != "Heatmap":
        x_col = st.selectbox("X-Axis", df.columns)
        y_col = st.selectbox("Y-Axis", df.columns)
    else:
        x_col = y_col = None

    if st.button("📈 Generate Chart"):
        try:
            if chart_type == "Bar":
                plot_bar(df, x_col, y_col)
            elif chart_type == "Line":
                plot_line(df, x_col, y_col)
            elif chart_type == "Scatter":
                plot_scatter(df, x_col, y_col)
            elif chart_type == "Pie":
                plot_pie(df, x_col, y_col)
            elif chart_type == "Heatmap":
                plot_heatmap(df)
        except Exception as e:
            st.error(f"❌ Error: {e}")

    #  Persistent Chat Memory Section with Clear Button

    st.markdown("---")
    st.subheader("💬 Chat with the Smart Data Analyst")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "system",
                "content": (
                    "You are a helpful data analyst. Answer naturally in short paragraphs. "
                    "Use bullet points when needed. Suggest charts and summarize patterns clearly. "
                    "Be concise and helpful for any questions about the uploaded dataset."
                )
            },
            {
                "role": "user",
                "content": f"Dataset columns: {', '.join(df.columns)}"
            }
        ]

    if st.button("🩹 Clear Chat"):
        st.session_state.chat_history = [
            {
                "role": "system",
                "content": (
                    "You are a helpful data analyst. Answer naturally in short paragraphs. "
                    "Use bullet points when needed. Suggest charts and summarize patterns clearly. "
                    "Be concise and helpful for any questions about the uploaded dataset."
                )
            },
            {
                "role": "user",
                "content": f"Dataset columns: {', '.join(df.columns)}"
            }
        ]
        st.rerun()

    for msg in st.session_state.chat_history[2:]:
        if msg["role"] == "user":
            st.markdown(f"**🧑‍💼 You:** {msg['content']}")
        elif msg["role"] == "assistant":
            st.markdown(f"**🤖 Analyst:** {msg['content']}")

    user_chat = st.chat_input("Ask a question about the data...")

    if user_chat:
        st.session_state.chat_history.append({"role": "user", "content": user_chat})
        try:
            reply = ask_local_llm(st.session_state.chat_history)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            st.rerun()
        except Exception as e:
            st.error(f"LLM Error: {e}")

else:
    st.info("📌 Please upload a CSV file from the sidebar to get started.")