import streamlit as st
from transformers import pipeline
from utils import clean_text

@st.cache_resource(show_spinner=False)
def load_model(model_name: str):
    return pipeline(
        task="summarization",
        model=model_name,
        tokenizer=model_name
    )

def summarize(text: str, model_name: str, max_len: int, min_len: int) -> str:
    text = clean_text(text)
    model = load_model(model_name)

    output = model(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return output[0]["summary_text"]
