import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(page_title="AI Job Market Analysis", layout="wide")

st.title("🤖 AI Job Rising Dashboard (Last 5 Months)")
st.write("Visualizing the growth of AI roles across top tech companies.")

# Load the dataset
try:
    df = pd.read_csv('Aijobdata.csv')
    
    # Sidebar Filters
    st.sidebar.header("Filter Data")
    industries = st.sidebar.multiselect(
        "Select Industry", 
        options=df["Industry"].unique(), 
        default=df["Industry"].unique()
    )
    
    filtered_df = df[df["Industry"].isin(industries)]

    # Layout: Top Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Companies", len(filtered_df["Company"].unique()))
    col2.metric("Total Postings", filtered_df["Job_Postings"].sum())
    col3.metric("Avg Salary", f"${filtered_df['Avg_Salary_USD'].mean():,.0f}")

    # Layout: Charts
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("Job Postings Trend")
        fig, ax = plt.subplots()
        # Grouping by month to see rising trend
        trend = filtered_df.groupby("Month")["Job_Postings"].sum().reset_index()
        # Ensuring months are in logical order for a 5-month view
        sns.lineplot(data=trend, x="Month", y="Job_Postings", marker="o", color="#0078D4", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with chart_col2:
        st.subheader("Industry-wise Salary Distribution")
        fig, ax = plt.subplots()
        sns.barplot(data=filtered_df, x="Industry", y="Avg_Salary_USD", palette="viridis", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Detailed Data View
    st.subheader("Company Wise Breakdown")
    st.dataframe(filtered_df, use_container_width=True)

except FileNotFoundError:
    st.error("Error: 'Aijobdata.csv' not found. Please ensure the file is in the same directory.")
