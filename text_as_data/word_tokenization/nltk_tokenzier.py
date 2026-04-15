from nltk.tokenize import (
    word_tokenize,
    wordpunct_tokenize,
    TreebankWordTokenizer,
)

text = "Dr. Smith's patients don't like waiting. It's 3:30pm!"

# Different NLTK tokenizers
nltk_word = word_tokenize(text) 
nltk_wordpunct = wordpunct_tokenize(text)
nltk_treebank = TreebankWordTokenizer().tokenize(text)

print("\n", nltk_word)
print("\n",nltk_wordpunct)
print("\n",nltk_treebank)