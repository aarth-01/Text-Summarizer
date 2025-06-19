## 📝 Text Summarization using NLTK

This is a basic Python project that performs **extractive text summarization** using the **Natural Language Toolkit (NLTK)** library. The user can input a large text and specify the number of paragraphs they want the summary to be compressed into.

## 🚀 Features

- Summarizes long-form text into concise form.
- Users can select how many paragraphs the summary should contain.
- Uses NLTK for tokenization, stopwords removal, and frequency-based scoring.

## 📌 Requirements
- Python 3.x
- NLTK

## To install NLTK:
pip install nltk

## To download required NLTK resources (run once):
python
import nltk
nltk.download('punkt')
nltk.download('stopwords')

## How It Works
Tokenizes the input into sentences and words.
Removes stopwords.
Calculates word frequencies.
Scores sentences based on word frequency.
Selects top-ranked sentences for the summary.
Groups them into user-defined paragraph count.

## File Structure
text_summarization/
│
├── first_python.py      # Main summarization script
├── sample_input.txt     # Example input file (optional)
└── README.md            # Project overview
