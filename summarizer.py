from transformers import pipeline
from utils import clean_text

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=130, min_length=30):
    cleaned_text = clean_text(text)

    summary = summarizer(
        cleaned_text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]["summary_text"]