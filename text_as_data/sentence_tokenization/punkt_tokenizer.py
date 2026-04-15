import nltk

# Download the punkt tokenizer data if needed
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)

from nltk.tokenize import sent_tokenize

# Test texts
test_texts = [
    "Dr. Smith went to Washington. He met the president.",
    "I bought 3.5 lbs. of apples. They cost $4.99.",
    "The U.S. economy grew 2.5% in Q3. Experts were surprised.",
    "She asked, 'Are you coming?' He said yes.",
    "Visit us at www.example.com. We're open 24/7!",
]

punkt_results = [(text, sent_tokenize(text)) for text in test_texts]
print(punkt_results)

from nltk.tokenize.punkt import PunktSentenceTokenizer

# Access the trained parameters
tokenizer = PunktSentenceTokenizer()

# Examine some internal parameters
params = tokenizer._params

# Check if specific words are marked as abbreviations
test_words = ["dr", "mr", "inc", "vs", "jan", "approx"]
abbrev_status = [(word, word in params.abbrev_types) for word in test_words]
print(abbrev_status)