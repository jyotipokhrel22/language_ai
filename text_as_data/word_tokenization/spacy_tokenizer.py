import spacy
from nltk.tokenize import (
    word_tokenize,
    wordpunct_tokenize,
    TreebankWordTokenizer,
)

# Load English model (small version for speed)
nlp = spacy.load("en_core_web_sm")

text = "Dr. Smith's patients don't like waiting. It's 3:30pm!"

# Tokenize
doc = nlp(text)
spacy_tokens = [token.text for token in doc]

# spaCy also provides additional information
token_info = [
    (token.text, token.pos_, token.is_punct, token.is_stop) for token in doc
]
print(spacy_tokens)

# compare tokenizer

challenge_text = (
    "I can't believe she's already gone! We'll miss her. #sad @friends"
)

# Tokenize with different tools
results = {
    "Whitespace": challenge_text.split(),
    "NLTK word_tokenize": word_tokenize(challenge_text),
    "NLTK Treebank": TreebankWordTokenizer().tokenize(challenge_text),
    "spaCy": [t.text for t in nlp(challenge_text)],
}
print("\n", results)