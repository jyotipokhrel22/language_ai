# Convert character to ASCII
print(ord('A'))  # Output: 65

# Convert ASCII to character
print(chr(97))   # Output: 'a'

# Check if a string is pure ASCII
my_string = "Hello"
is_ascii = my_string.isascii() # Returns True

# Exploring Unicode code points
characters = [
    ("A", "Latin capital A"),
    ("é", "Latin small e with acute"),
    ("α", "Greek small alpha"),
    ("中", "CJK character for middle"),
    ("😀", "Grinning face emoji"),
    ("𝕳", "Mathematical double-struck H"),
]

# Get code point information
code_points = [(char, name, ord(char)) for char, name in characters]
print(code_points)

def show_utf8_encoding(char):
    """Display how a character is encoded in UTF-8."""
    code_point = ord(char)
    utf8_bytes = char.encode("utf-8")

    # Format bytes as binary
    binary = " ".join(f"{b:08b}" for b in utf8_bytes)
    hex_repr = " ".join(f"{b:02x}" for b in utf8_bytes)

    return {
        "char": char,
        "code_point": code_point,
        "num_bytes": len(utf8_bytes),
        "binary": binary,
        "hex": hex_repr,
    }


# Test with characters from different ranges
test_chars = ["A", "é", "中", "😀"]
encodings = [show_utf8_encoding(c) for c in test_chars]
print(f"\nEncodings:  {encodings}")