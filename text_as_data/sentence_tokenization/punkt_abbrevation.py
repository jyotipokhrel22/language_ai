import math
import re
from collections import defaultdict


class PunktLearner:
    """Simplified Punkt-style abbreviation learner."""

    def __init__(self):
        self.word_counts = defaultdict(int)
        self.word_with_period_counts = defaultdict(int)
        self.total_words = 0

    def train(self, text):
        """Learn abbreviation patterns from text."""
        # Tokenize simply by whitespace and punctuation
        tokens = re.findall(r"\b\w+\.?|\S", text)

        for token in tokens:
            if token.isalpha() or (
                token.endswith(".") and token[:-1].isalpha()
            ):
                self.total_words += 1
                word = token.rstrip(".").lower()
                self.word_counts[word] += 1

                if token.endswith("."):
                    self.word_with_period_counts[word] += 1

    def abbreviation_score(self, word):
        """Calculate likelihood that word is an abbreviation."""
        word = word.lower().rstrip(".")

        total = self.word_counts[word]
        with_period = self.word_with_period_counts[word]

        if total == 0:
            return 0.0

        # Period affinity: fraction of occurrences with period
        period_ratio = with_period / total

        # Length penalty: shorter words score higher
        length_factor = 1.0 / (len(word) + 1)

        # Frequency weighting: more occurrences = more confidence
        frequency_factor = math.log(total + 1)

        # Combine all factors
        score = period_ratio * length_factor * frequency_factor

        return score

    def get_likely_abbreviations(self, threshold=0.1):
        """Return words likely to be abbreviations."""
        abbrevs = []
        for word in self.word_counts:
            score = self.abbreviation_score(word)
            if score > threshold:
                abbrevs.append((word, score))

        return sorted(abbrevs, key=lambda x: -x[1])

# Training corpus with various abbreviations
training_text = """
Dr. Smith and Mrs. Jones met at the U.S. Capitol building.
The meeting was scheduled for 3 p.m. on Jan. 15th.
Mr. Brown, who works at Corp. headquarters, also attended.
Dr. Smith presented findings from the Ph.D. program.
Mrs. Jones discussed the approx. $5M budget for the dept.
The U.S. government approved the proposal. Dr. Smith was pleased.
Mr. Brown noted that Corp. profits exceeded expectations.
The meeting ended at 5 p.m. Everyone agreed it was productive.
"""

learner = PunktLearner()
learner.train(training_text)

# Get learned abbreviations
abbreviations = learner.get_likely_abbreviations(threshold=0.05)
print(abbreviations)