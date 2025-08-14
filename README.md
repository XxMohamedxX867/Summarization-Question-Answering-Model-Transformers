# 🧠 Text Summarizer & Question Answering

A powerful NLP application that performs both **Text Summarization** and **Question Answering** using state-of-the-art Hugging Face models. Built with Streamlit for an intuitive user interface and includes a Jupyter notebook for experimentation.

## ✨ Features

- **📝 Text Summarization**: Generate concise summaries from long text using DistilBART
- **❓ Question Answering**: Get precise answers to questions based on provided context
- **🎨 Streamlit UI**: Clean, responsive web interface for easy interaction

## 🏗️ Project Structure

```
Text Summarizer & Question Answering/
├── app.py                 # Streamlit web application
├── main.ipynb            # Jupyter notebook for testing
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
└── env_QA/               # Virtual environment directory
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd "Text Summarizer & Question Answering"
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv env_QA
   env_QA\Scripts\activate
   
   # macOS/Linux
   python -m venv env_QA
   source env_QA/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 💻 Usage

### Streamlit App
The main application provides an intuitive interface where you can:
- Switch between Summarization and Question Answering modes
- Input text for summarization
- Provide context and questions for Q&A
- View results in real-time

### Jupyter Notebook
Open `main.ipynb` for interactive experimentation with the models.

### Programmatic Usage

#### Text Summarization
```python
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

text = """
PG&E stated it scheduled the blackouts in response to forecasts for high winds
amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were
scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow.
"""

summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
print(summary[0]['summary_text'])
```

#### Question Answering
```python
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

context = "Hugging Face is a company based in New York City that develops tools for building machine learning applications."
question = "Where is Hugging Face based?"

answer = qa_pipeline(question=question, context=context)
print(f"Answer: {answer['answer']}")
print(f"Confidence: {answer['score']:.2f}")
```

## 🧩 Models Used

- **Summarization**: `sshleifer/distilbart-cnn-12-6`
  - Lightweight DistilBART model fine-tuned on CNN/DailyMail
  - Fast inference with good summarization quality
  
- **Question Answering**: `distilbert-base-uncased-distilled-squad`
  - Distilled BERT model fine-tuned on SQuAD dataset
  - Efficient for extractive question answering

## 📋 Requirements

- **streamlit** - Web application framework
- **transformers** - Hugging Face transformers library
- **torch** - PyTorch backend for transformers


## 🔗 Resources

- [Hugging Face](https://huggingface.co/google/flan-t5-small) Hugging Face Model
- [Streamlit](https://streamlit.io/) for the intuitive web framework

