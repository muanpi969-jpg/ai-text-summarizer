import streamlit as st
from summarizer import summarize
from utils import count_words, timed

st.set_page_config(
    page_title="Text Summarizer",
    layout="centered"
)

st.title("Text Summarization")
st.caption("Abstractive summarization using transformer models")

# Model selection (aligned with your CV)
model_map = {
    "BART (balanced)": "facebook/bart-large-cnn",
    "T5 (lightweight)": "t5-small"
}

model_label = st.selectbox("Model", list(model_map.keys()))
model_name = model_map[model_label]

# Input
text = st.text_area("Input text", height=260)

# Word count (raw input)
if text:
    st.markdown(f"**Input word count:** {count_words(text)}")

# Controls
max_len = st.slider("Max length", 50, 300, 130)
min_len = st.slider("Min length", 10, 100, 30)

# Run
if st.button("Generate"):
    if not text.strip():
        st.warning("Input required.")
    else:
        with st.spinner("Running model..."):
            summary, latency = timed(
                summarize,
                text,
                model_name,
                max_len,
                min_len
            )

        st.subheader("Summary")
        st.write(summary)

        st.caption(f"Inference time: {latency}s")
