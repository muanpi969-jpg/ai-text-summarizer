import streamlit as st
from transformers import pipeline
from utils import clean_text

@st.cache_resource
def load_summarizer(model_name):
    # This ensures the task and framework are explicitly defined
    return pipeline("summarization", model=model_name, framework="pt")

def summarize_text(text, model_name="facebook/bart-large-cnn", max_length=130, min_length=30):
    cleaned_text = clean_text(text)
    summarizer = load_summarizer(model_name)
    
    summary = summarizer(
        cleaned_text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return summary[0]['summary_text']
