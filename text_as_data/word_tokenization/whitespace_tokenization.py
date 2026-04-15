def whitespace_tokenize(text):
    """Split text on whitespace."""
    return text.split()


# Test on clean text
clean_text = "The quick brown fox jumps over the lazy dog"
clean_tokens = whitespace_tokenize(clean_text)

# Test on messy text
messy_text = "Hello,   world!  How   are  you?"
messy_tokens = whitespace_tokenize(messy_text)

print(clean_tokens)
print(messy_tokens)