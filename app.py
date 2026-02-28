import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="AI Text Summarizer", layout="centered")

st.title("📝 AI Text Summarizer")
st.markdown("Summarize long articles using a Transformer-based model.")

text_input = st.text_area("Enter your text below:", height=300)

max_length = st.slider("Maximum Summary Length", 50, 300, 130)
min_length = st.slider("Minimum Summary Length", 10, 100, 30)

if st.button("Generate Summary"):
    if text_input.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_text(
                text_input,
                max_length=max_length,
                min_length=min_length
            )
        st.success("Summary Generated!")
        st.subheader("Summary:")
        st.write(summary)