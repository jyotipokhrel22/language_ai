# spaCy provides robust multilingual support and is worth understanding as an alternative to NLTK Punkt, particularly for applications that need tight integration with other NLP components. While NLTK's Punkt works purely from statistical patterns over raw text, spaCy's full language models use dependency parsing to determine sentence boundaries. 

# Dependency parsing = Analyzing grammatical relationships between words to understand sentence structure.

import spacy

# Load English model
try:
    nlp_en = spacy.load("en_core_web_sm")
except OSError:
    # Model not installed, use blank
    nlp_en = spacy.blank("en")
    nlp_en.add_pipe("sentencizer")

# Test with English
english_text = "Dr. Smith works at U.S. Steel. He's been there for 10 years."
doc = nlp_en(english_text)
spacy_sentences = [sent.text for sent in doc.sents]
print(spacy_sentences)