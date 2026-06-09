import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load IMDb dataset
dataset = load_dataset("imdb")

train_df = pd.DataFrame(dataset['train'])

# Create sentiment labels
train_df['sentiment'] = train_df['label'].map({
    0: 'negative',
    1: 'positive'
})

# Dashboard Title
st.title("IMDb Sentiment Analysis Dashboard")

# Dataset Overview
st.header("Dataset Overview")

st.write("Total Reviews:", len(train_df))

positive_count = len(
    train_df[train_df['sentiment'] == 'positive']
)

negative_count = len(
    train_df[train_df['sentiment'] == 'negative']
)

st.write("Positive Reviews:", positive_count)
st.write("Negative Reviews:", negative_count)

# Sentiment Distribution Chart
st.header("Sentiment Distribution")

fig, ax = plt.subplots()

train_df['sentiment'].value_counts().plot(
    kind='bar',
    ax=ax
)

plt.title("Sentiment Distribution")

st.pyplot(fig)

# Sample Reviews
st.header("Sample Reviews")

st.dataframe(
    train_df[['text', 'sentiment']].head(10)
)