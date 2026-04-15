# A regular expression (regex) is a sequence of characters that defines a search pattern. Think of it as a tiny programming language embedded within Python, specialized for matching and manipulating text. Regex is not unique to Python. The same core syntax works in Java, JavaScript, Ruby, Perl, Go, and dozens of other languages, as well as in command-line tools like grep, sed, and awk.

import re

text = "Contact us at support@example.com or sales@example.com"

# re.search() - Find first match
first_match = re.search(r"\w+@\w+\.\w+", text)

# re.findall() - Find all matches, return list of strings
all_matches = re.findall(r"\w+@\w+\.\w+", text)

# re.finditer() - Find all matches, return iterator of match objects
match_objects = list(re.finditer(r"\w+@\w+\.\w+", text))

# re.sub() - Replace matches
replaced = re.sub(r"\w+@\w+\.\w+", "[EMAIL]", text)

# re.split() - Split by pattern
parts = re.split(r"\s+", "Hello   world  foo")

print(first_match)
print(all_matches)
print(match_objects)
print(replaced)
print(parts)

# Output : <re.Match object; span=(14, 33), match='support@example.com'>
# ['support@example.com', 'sales@example.com']
# [<re.Match object; span=(14, 33), match='support@example.com'>, <re.Match object; span=(37, 54), match='sales@example.com'>]
# Contact us at [EMAIL] or [EMAIL]
# ['Hello', 'world', 'foo']