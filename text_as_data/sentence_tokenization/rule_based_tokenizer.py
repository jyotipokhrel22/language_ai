import re

class SimpleSegmenter:
    """A rule-based sentence segmenter."""

    def __init__(self):
        # Common abbreviations that don't end sentences
        self.abbreviations = {
            "mr",
            "mrs",
            "ms",
            "dr",
            "prof",
            "sr",
            "jr",
            "vs",
            "etc",
            "viz",
            "al",
            "eg",
            "ie",
            "cf",
            "inc",
            "ltd",
            "corp",
            "co",
            "jan",
            "feb",
            "mar",
            "apr",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
            "st",
            "rd",
            "th",
            "ave",
            "blvd",
            "approx",
            "dept",
            "est",
            "min",
            "max",
            "govt",
            "natl",
            "intl",
        }

        # Titles that precede names
        self.titles = {
            "mr",
            "mrs",
            "ms",
            "dr",
            "prof",
            "rev",
            "gen",
            "col",
            "lt",
            "sgt",
        }

    def is_abbreviation(self, token):
        """Check if token is a known abbreviation."""
        # Remove trailing period for comparison
        word = token.rstrip(".").lower()
        return word in self.abbreviations

    def is_likely_sentence_end(self, before, punct, after):
        """Determine if punctuation likely ends a sentence."""
        # Question marks and exclamation points usually end sentences
        if punct in "?!":
            # Unless inside quotes followed by lowercase
            if after and after[0].islower():
                return False
            return True

        # For periods, apply heuristics
        if punct == ".":
            # Check if preceding word is abbreviation
            words_before = before.split()
            if words_before:
                last_word = words_before[-1]
                if self.is_abbreviation(last_word + "."):
                    # Abbreviation followed by lowercase = not sentence end
                    if after and after.strip() and after.strip()[0].islower():
                        return False
                    # Abbreviation followed by capital might still be sentence end
                    # Use additional heuristics...

            # Period followed by capital letter suggests sentence boundary
            if after and after.strip():
                first_char = after.strip()[0]
                if first_char.isupper():
                    return True

        return False

def segment(self, text):
    """Split text into sentences."""
    sentences = []
    current = []

    # Pattern to find potential sentence boundaries
    # Matches period, question mark, or exclamation followed by space and capital
    boundary_pattern = re.compile(r"([.!?])\s+")

    # Split on potential boundaries
    parts = boundary_pattern.split(text)

    i = 0
    while i < len(parts):
        current.append(parts[i])

        if i + 1 < len(parts) and parts[i + 1] in ".!?":
            punct = parts[i + 1]
            before = "".join(current)
            after = parts[i + 2] if i + 2 < len(parts) else ""

            if self.is_likely_sentence_end(before, punct, after):
                current.append(punct)
                sentences.append("".join(current).strip())
                current = []
                i += 2
            else:
                current.append(punct)
                i += 2
        else:
            i += 1

    # Add remaining text
    if current:
        remaining = "".join(current).strip()
        if remaining:
            sentences.append(remaining)

    return sentences


# Add method to class
SimpleSegmenter.segment = segment

segmenter = SimpleSegmenter()

test_texts = [
    "Hello world. How are you?",
    "Dr. Smith went to Washington. He met the president.",
    "I paid $3.50 for coffee. It was expensive.",
    "She works at U.S. Steel Corp. The company is huge.",
]

results = [(text, segmenter.segment(text)) for text in test_texts]
print(results)