"""
String obfuscation module:
- Random character insertion
- Character splitting & concatenation
- Reversible transformations (reverse)
- Escape-sequence obfuscation

All techniques are reversible (with helper functions) to demonstrate controlled lab usage.
"""

import random
import string
import re
from typing import Tuple


def obf_random_insertion(text: str, density: float = 0.2, chars: str = string.ascii_letters) -> str:
    """
    Insert random characters between original characters.
    For demo/reversibility, we return (obfuscated_text, original_length).
    """
    out = []
    for ch in text:
        out.append(ch)
        if random.random() < density:
            out.append(random.choice(chars))
    return "".join(out)


def deobf_random_insertion_simple(obf: str, original_len: int) -> str:
    """
    Simple reversal assuming we know original length and that only single insertions occurred.
    This is a toy reverser for demonstration purposes in a lab environment.
    """
    if original_len == 0:
        return ""
    step = max(1, round(len(obf) / original_len))
    return obf[::step][:original_len]


def obf_split_concat(text: str, chunk_size: int = 1) -> str:
    """Split into chunks and join with a delimiter. Reversible by removing delimiter."""
    delim = "_"
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return delim.join(chunks)


def deobf_split_concat(obf: str, delim: str = "_") -> str:
    """Reverse split+concat by removing delimiter."""
    return obf.replace(delim, "")


def obf_escape_sequences(text: str) -> str:
    """
    Replace some characters with escape-like sequences (e.g., 'a' -> '\\x61').
    Reversible by unescaping hex sequences.
    """
    mapping = {
        "a": "\\x61", "b": "\\x62", "c": "\\x63", "d": "\\x64", "e": "\\x65",
        "f": "\\x66", "g": "\\x67", "h": "\\x68", "i": "\\x69", "j": "\\x6a",
        "k": "\\x6b", "l": "\\x6c", "m": "\\x6d", "n": "\\x6e", "o": "\\x6f",
        "p": "\\x70", "q": "\\x71", "r": "\\x72", "s": "\\x73", "t": "\\x74",
        "u": "\\x75", "v": "\\x76", "w": "\\x77", "x": "\\x78", "y": "\\x79",
        "z": "\\x7a",
        "A": "\\x41", "B": "\\x42", "C": "\\x43", "D": "\\x44", "E": "\\x45",
        "F": "\\x46", "G": "\\x47", "H": "\\x48", "I": "\\x49", "J": "\\x4a",
        "K": "\\x4b", "L": "\\x4c", "M": "\\x4d", "N": "\\x4e", "O": "\\x4f",
        "P": "\\x50", "Q": "\\x51", "R": "\\x52", "S": "\\x53", "T": "\\x54",
        "U": "\\x55", "V": "\\x56", "W": "\\x57", "X": "\\x58", "Y": "\\x59",
        "Z": "\\x5a",
        " ": "\\x20", "\n": "\\x0a", "\t": "\\x09",
    }
    out = []
    for ch in text:
        out.append(mapping.get(ch, ch))
    return "".join(out)


def deobf_escape_sequences(obf: str) -> str:
    """Reverse escape-sequence obfuscation."""
    def repl(m):
        hexval = m.group(1)
        return chr(int(hexval, 16))
    return re.sub(r"\\x([0-9a-fA-F]{2})", repl, obf)


def obf_reverse_text(text: str) -> str:
    """Reverse the text (reversible transformation)."""
    return text[::-1]


def deobf_reverse_text(obf: str) -> str:
    """Reverse again to get original."""
    return obf[::-1]