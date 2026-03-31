# Transformer-Based Text Summarization System

🔗 Live Demo: https://muanpi-ai-text-summarizer.streamlit.app/


## Overview

This project implements an abstractive text summarization system using transformer-based encoder–decoder models.  
It focuses on controlled inference, model comparison, and deployment of NLP systems in a real-world setting.

The goal was not only to use pretrained models, but to understand how architectural choices and decoding strategies affect summary quality, efficiency, and behavior.


## Core Functionality

- Abstractive summarization using transformer models  
- Model switching between BART and T5  
- Input word count tracking before summarization  
- Adjustable output length (min/max tokens)  
- Inference latency measurement  
- Streamlit-based deployment for interactive use  


## Model Selection

- **BART (facebook/bart-large-cnn)**  
  Produces balanced summaries with stronger structural coherence.

- **T5 (t5-small)**  
  Faster and lighter, but tends to generate simpler and shorter summaries.

These differences reflect trade-offs between model size, inference speed, and abstraction level.


## System Design

The application follows a modular structure:

- `summarizer.py` → model loading and inference  
- `utils.py` → preprocessing and timing utilities  
- `app.py` → interface and user interaction  

### Design Decisions

- Cached model loading to avoid repeated initialization  
- Deterministic decoding (`do_sample=False`) for stable outputs  
- Lightweight preprocessing to normalize input text  
- Explicit control over summary length  
- Separation of UI and inference logic  

These choices were made to balance performance, reproducibility, and clarity.


## Observations

During testing:

- BART produced more coherent summaries for structured inputs  
- T5 was significantly faster but less detailed  
- Output quality depends heavily on decoding configuration and input length  

This highlights the importance of aligning model choice with application constraints.


## Limitations

- Transformer token limits restrict very long inputs  
- No fine-tuning on domain-specific datasets  
- Summaries can be partially extractive depending on model behavior  
- No quantitative evaluation metrics (e.g., ROUGE) implemented  


## Future Work

- Implement ROUGE-based evaluation  
- Add long-text chunking for extended inputs  
- Compare decoding strategies (greedy vs sampling)  
- Extend to additional transformer models  
- Expose as an API for scalable usage  


## Technical Stack

- Python  
- Streamlit  
- Hugging Face Transformers  
- PyTorch  


## Notes

This project involved debugging deployment environments, managing dependency compatibility, and handling runtime constraints.  
It reflects an applied understanding of how modern NLP systems behave outside of controlled environments.
