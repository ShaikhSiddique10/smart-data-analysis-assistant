import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#  Bar Chart
def plot_bar(df, x_col, y_col):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=x_col, y=y_col, data=df)
    plt.xticks(rotation=45)
    plt.title(f"{y_col} by {x_col}")
    st.pyplot(plt.gcf())

#  Line Chart
def plot_line(df, x_col, y_col):
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=x_col, y=y_col, data=df)
    plt.xticks(rotation=45)
    plt.title(f"{y_col} over {x_col}")
    st.pyplot(plt.gcf())

#  Scatter Plot
def plot_scatter(df, x_col, y_col):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=x_col, y=y_col, data=df)
    plt.xticks(rotation=45)
    plt.title(f"{y_col} vs {x_col}")
    st.pyplot(plt.gcf())

#  Pie Chart
def plot_pie(df, category_col, value_col):
    pie_data = df.groupby(category_col)[value_col].sum()
    plt.figure(figsize=(6, 6))
    plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
    plt.title(f"{value_col} distribution by {category_col}")
    st.pyplot(plt.gcf())

#  Heatmap
def plot_heatmap(df):
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.shape[1] < 2:
        st.warning("❌ Heatmap needs at least 2 numeric columns.")
        return
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    st.pyplot(plt.gcf())
