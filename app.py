import streamlit as st
from transformers import pipeline

# Load model once
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

flan = load_model()

# Streamlit UI
st.set_page_config(page_title="FLAN-T5 NLP App", page_icon="🤖", layout="centered")
st.title("🤖 AI Summarization & Question Answering")
st.write("Powered by `google/flan-t5-small` — one model for multiple NLP tasks!")

# Task selection
task = st.radio("Choose a task:", ["Summarization", "Question Answering"])

# Inputs
context = st.text_area("Enter your text:", height=150)

if task == "Summarization":
    if st.button("Summarize"):
        if context.strip():
            with st.spinner("Generating summary..."):
                summary = flan(f"Summarize: {context}", max_length=80)[0]['generated_text']
            st.success("**Summary:**")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

elif task == "Question Answering":
    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        if context.strip() and question.strip():
            with st.spinner("Finding answer..."):
                answer = flan(f"Answer the question based on the text: {context}\nQuestion: {question}")[0]['generated_text']
            st.success("**Answer:**")
            st.write(answer)
        else:
            st.warning("Please enter both text and a question.")
