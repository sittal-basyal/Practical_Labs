"""
Lab 06 - Program to illustrate concepts of NLP using NLTK

Demonstrates the following fundamental NLP preprocessing steps:
    1. Sentence Tokenization
    2. Word Tokenization
    3. Stopword Removal
    4. Stemming (Porter Stemmer)
    5. Lemmatization (WordNet Lemmatizer)
    6. Part-of-Speech (POS) Tagging

Run once with internet access so NLTK can download the required
corpora/models (punkt, stopwords, wordnet, averaged_perceptron_tagger).
"""
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

text = "Artificial Intelligence is transforming the world. Natural Language Processing helps machines understand human language."

# 1. Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# 2. Word Tokenization
words = word_tokenize(text)
print("Words:", words)

# 3. Stopword Removal
stop = set(stopwords.words("english"))
filtered = [w for w in words if w.lower() not in stop and w.isalnum()]
print("Without Stopwords:", filtered)

# 4. Stemming
stemmer = PorterStemmer()
print("Stemming:", [stemmer.stem(w) for w in filtered])

# 5. Lemmatization
lemmatizer = WordNetLemmatizer()
print("Lemmatization:", [lemmatizer.lemmatize(w) for w in filtered])

# 6. POS Tagging
print("POS Tagging:", nltk.pos_tag(words))