import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="DataViz Dashboard", layout="wide")

st.title("📊 Simple Dataset Visualizer")
st.write("Upload a CSV file to explore and visualize your data instantly.")

# File uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Sidebar - Data Preview Settings
    st.sidebar.header("Settings")
    if st.sidebar.checkbox("Show Raw Data"):
        st.subheader("Raw Data")
        st.dataframe(df.head(10))

    # Visualization Section
    st.subheader("Custom Visualizations")
    
    columns = df.columns.tolist()
    
    col1, col2 = st.columns(2)
    
    with col1:
        chart_type = st.selectbox("Select Chart Type", ["Line Plot", "Bar Chart", "Scatter Plot", "Histogram"])
        x_axis = st.selectbox("Select X-axis", columns)
        
    with col2:
        y_axis = st.selectbox("Select Y-axis", columns)
        color = st.color_picker("Pick a chart color", "#6C63FF")

    # Plotting Logic
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if chart_type == "Line Plot":
        ax.plot(df[x_axis], df[y_axis], color=color, marker='o')
    elif chart_type == "Bar Chart":
        ax.bar(df[x_axis], df[y_axis], color=color)
    elif chart_type == "Scatter Plot":
        ax.scatter(df[x_axis], df[y_axis], color=color)
    elif chart_type == "Histogram":
        ax.hist(df[x_axis], bins=20, color=color, edgecolor="white")
        plt.xlabel(x_axis)

    # Aesthetics
    plt.xticks(rotation=45)
    plt.title(f"{chart_type} of {y_axis} vs {x_axis}")
    plt.tight_layout()

    # Display the plot
    st.pyplot(fig)

else:
    st.info("💡 Please upload a CSV file from the sidebar to get started.")
