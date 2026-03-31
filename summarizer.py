from transformers import pipeline
from utils import clean_text

def summarize_text(text, model_name="facebook/bart-large-cnn", max_length=130, min_length=30):
    cleaned_text = clean_text(text)
    
    # We add framework="pt" to ensure it uses PyTorch explicitly
    summarizer = pipeline(
        "summarization", 
        model=model_name, 
        framework="pt"
    )

    summary = summarizer(
        cleaned_text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]['summary_text']
