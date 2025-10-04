# PES-Projects
Author - Sameer Manvi
# Sentiment Analyzer

## Project Overview
This project is a simple command-line tool that analyzes the sentiment of a given text. It classifies the text as **Positive**, **Negative**, or **Neutral** using Python and the TextBlob library. This project was developed as part of my application to the HackerSpace Club (HSP) at PES University.

## Features
*   Analyzes text input directly from the command line.
*   Categorizes sentiment into three distinct labels.
*   Built with Python, making it accessible and easy to run.

## How to Get Started

### Prerequisites
Make sure you have Python 3 installed on your system.

### Installation
1.  **Clone the repository (or download the files):**
    If you're using Git, you can clone the repository to get a local copy.

2.  **Install the necessary library:**
    This project depends on the `TextBlob` library. You can install it using pip:
    ```
    pip install textblob
    ```
    python3 -m pip install textblob

## How to Use the Program
Once the installation is complete, you can run the script from your terminal:

## python analyzer.py
The program will prompt you to enter a sentence, and it will return the analyzed sentiment.

## How It Works
The core of this project is the **TextBlob** library, which provides a simple API for common Natural Language Processing (NLP) tasks. When you provide text to the program, TextBlob analyzes it and returns a `polarity` score, which is a number between -1 (very negative) and 1 (very positive).

My script then uses this score to classify the sentiment:
*   **Positive:** Polarity score > 0
*   **Negative:** Polarity score < 0
*   **Neutral:** Polarity score = 0

## Future Improvements
Given more time, I would love to expand on this project in a few ways:
*   **Build a Web Interface:** Create a simple front-end with Flask or Django so anyone can use the analyzer from their web browser.
*   **Train a Custom Model:** Use a dataset of labeled text (like movie reviews) to train a more specialized sentiment analysis model.
*   **Analyze Larger Datasets:** Adapt the tool to analyze sentiment from a file (like a CSV of tweets) instead of just single sentences.
