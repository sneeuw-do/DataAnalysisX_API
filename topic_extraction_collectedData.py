import pandas as pd
import re
import subprocess
import sys
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import nltk
from nltk.corpus import stopwords

# Once needed for the first start
nltk.download("stopwords")
stop_words = stopwords.words("german")

# Loading CSV sheet
df = pd.read_csv("C:/Users/Sebastian/PDA/original_tweets.csv")
texts = df["text"].dropna().tolist()

#Spacy NLP
try:
    nlp = spacy.load("de_core_news_sm")
except OSError:
    print("automatic installation of spacy...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "de_core_news_sm"])
    nlp = spacy.load("de_core_news_sm")

#Adding more skipped words
from spacy.lang.de.stop_words import STOP_WORDS as SPACY_STOP_WORDS

extra_nonused_words = {
    "rt", "https", "http", "co", "amp", "frankfurt", "main", "web", "nachricht",
    "frau", "mann", "user", "heute", "gestern", "jetzt", "noch", "mal", "ipyy", "arslana",
    "rjzrs", "rjv", "sfqdsejxrv"
}

all_stopwords = set(word.lower() for word in SPACY_STOP_WORDS).union(set(extra_nonused_words))

# Clearing the text in the CSV file
def preprocess_with_spacy(text):
    text = re.sub(r"http\\S+", "", text.lower())
    text = re.sub(r"[^a-zäöüß\\s]", " ", text)
    doc = nlp(text)
    tokens = [
        token.lemma_.lower() for token in doc
        if token.pos_ in {"NOUN", "PROPN", "VERB"}
           and token.lemma_.lower() not in all_stopwords
           and len(token.lemma_) > 2
    ]
    return " ".join(tokens)

cleaned_texts = [preprocess_with_spacy(t) for t in texts]

# TF-IDF-vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(cleaned_texts)

# NMF for the topic extraction
nmf = NMF(n_components=5, random_state=42)
W = nmf.fit_transform(X)
H = nmf.components_
feature_names = vectorizer.get_feature_names_out()

# Top words for the top 5 topics
print("🔍 Top 5 Topics:")
for idx, topic in enumerate(H):
    top_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
    print(f"Thema {idx+1}: {', '.join(top_words)}")
