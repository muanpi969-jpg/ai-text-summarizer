🧠 Transformer-Based Abstractive Text Summarization System

🎓 Academic Positioning

This project was developed to explore real-world applications of Transformer architectures in Natural Language Processing (NLP).

As a prospective Computer Science student focusing on Artificial Intelligence and Machine Learning, I built this system to deepen my understanding of:
	•	Encoder–decoder transformer models
	•	Self-attention mechanisms
	•	Tokenization and sequence length constraints
	•	Inference pipeline optimization
	•	Practical deployment of large language models

Rather than only using pretrained models, I focused on understanding the architectural and computational trade-offs involved in transformer-based summarization.



🔬 Technical Foundations

1️⃣ Problem Type

This project implements abstractive text summarization, which differs from extractive summarization by generating new sentences rather than copying segments from the original text.

Abstractive summarization requires:
	•	Context modeling
	•	Long-range dependency tracking
	•	Semantic compression

These are achieved using transformer-based attention mechanisms.



2️⃣ Model Architecture

The system evaluates three transformer models:
	•	facebook/bart-large-cnn
	•	t5-small
	•	google/pegasus-xsum

All are encoder-decoder architectures trained on large corpora.

Core Concepts Applied:
	•	Multi-head self-attention
	•	Positional encoding
	•	Sequence-to-sequence generation
	•	Beam search inference



⚙️ Engineering Design

The project follows modular design principles:
summarizer.py   → model loading + inference
utils.py        → preprocessing
app.py          → user interface layer
Design decisions:
	•	Model is loaded once to optimize runtime efficiency
	•	Adjustable max/min token length
	•	Clean preprocessing to reduce noise
	•	Deterministic decoding (do_sample=False)

This reflects awareness of computational cost and inference performance.



📊 Model Comparison Insights

During experimentation, I observed:
	•	BART produced more coherent summaries for structured news content
	•	T5-small was computationally lighter but less detailed
	•	Pegasus performed well on concise inputs

This highlights the trade-off between:
	•	Model size
	•	Inference speed
	•	Output quality

Understanding these trade-offs is central to ML system design.



🚧 Limitations & Critical Analysis
	•	Token limit (~1024 tokens for BART)
	•	No domain-specific fine-tuning
	•	No quantitative evaluation metrics (e.g., ROUGE)
	•	Pretrained model biases may affect summary framing

Recognizing system limitations is essential in responsible AI development.



📈 Future Extensions (AI/ML Direction)

To further develop this into a research-oriented system:
	•	Fine-tune model on domain-specific dataset
	•	Implement ROUGE evaluation metrics
	•	Compare greedy decoding vs beam search
	•	Add multilingual transformer models
	•	Convert into REST API for scalable deployment



📚 Personal Learning Reflection

Building this project strengthened my understanding of how transformer architectures operate beyond theoretical explanations. I encountered environment compatibility issues, token length constraints, and model loading inefficiencies, which required debugging and system-level thinking.

This experience reinforced my interest in pursuing Computer Science with a focus on Artificial Intelligence and Machine Learning.