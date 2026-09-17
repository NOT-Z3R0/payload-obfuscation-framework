"""
Encoding module: Base64, XOR, ROT13.
Matches project requirement: Base64 encoding & decoding, XOR with user-defined key, ROT13 substitution.
"""

import base64
import codecs
from typing import Union


def encode_base64(data: bytes) -> bytes:
    """Base64 encode bytes."""
    return base64.b64encode(data)


def decode_base64(data: bytes) -> bytes:
    """Base64 decode bytes."""
    return base64.b64decode(data)


def encode_rot13_text(text: str) -> str:
    """ROT13 encode text (symmetric)."""
    return codecs.encode(text, "rot_13")


def decode_rot13_text(text: str) -> str:
    """ROT13 decode text (same as encode)."""
    return codecs.encode(text, "rot_13")


def xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR encrypt/encode bytes with a repeating key."""
    if not key:
        raise ValueError("XOR key must not be empty")
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))