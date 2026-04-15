# Sentence boundary detection (SBD) is the task of identifying the positions in text where one sentence ends and the next begins. It is also called sentence segmentation or sentence splitting.

# Analyze period usage in sample text
sample_text = """
Dr. Jane Smith, Ph.D., works at the U.S. Department of Energy.
She earned $125.5K last year. Her research on A.I. and M.L. is groundbreaking.
The project, funded by N.I.H., costs approx. $2.5M annually.
Visit her at www.energy.gov for more info. Contact: j.smith@energy.gov
"""

# Count different period types
import re

# Find all periods with context
period_contexts = []
for match in re.finditer(r".{0,10}\.(?:.{0,10})?", sample_text):
    context = match.group()
    period_contexts.append(context.strip())

# Count total periods
total_periods = sample_text.count(".")

# Count sentence-ending periods (rough heuristic: period followed by space and capital)
sentence_endings = len(re.findall(r"\.\s+[A-Z]", sample_text))

# Count decimal points
decimal_points = len(re.findall(r"\d\.\d", sample_text))

# Count URL/email periods
url_email_periods = len(re.findall(r"www\.|\.gov|\.com|@\w+\.", sample_text))

# Remaining are likely abbreviations
abbreviation_periods = (
    total_periods - sentence_endings - decimal_points - url_email_periods
)

print(total_periods)
print(decimal_points)
print(url_email_periods)
print(abbreviation_periods)
