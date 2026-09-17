"""
Basic sanity tests for the framework.
Run with: python -m unittest tests.test_framework
"""

import unittest

from src.encoders import encode_base64, decode_base64, encode_rot13_text, xor_bytes
from src.obfuscators import obf_split_concat, deobf_split_concat, obf_reverse_text, deobf_reverse_text
from src.detector import SignatureEngine


class TestEncoders(unittest.TestCase):

    def test_base64_roundtrip(self):
        data = b"hello world"
        enc = encode_base64(data)
        dec = decode_base64(enc)
        self.assertEqual(data, dec)

    def test_rot13_symmetry(self):
        text = "hello world"
        enc = encode_rot13_text(text)
        dec = encode_rot13_text(enc)  # ROT13 is symmetric
        self.assertEqual(text, dec)

    def test_xor_roundtrip(self):
        data = b"secret payload"
        key = b"mykey"
        enc = xor_bytes(data, key)
        dec = xor_bytes(enc, key)
        self.assertEqual(data, dec)


class TestObfuscators(unittest.TestCase):

    def test_split_concat_roundtrip(self):
        text = "hello world"
        obf = obf_split_concat(text, chunk_size=2)
        rev = deobf_split_concat(obf)
        self.assertEqual(text, rev)

    def test_reverse_roundtrip(self):
        text = "hello world"
        obf = obf_reverse_text(text)
        rev = deobf_reverse_text(obf)
        self.assertEqual(text, rev)


class TestDetector(unittest.TestCase):

    def test_signature_detection(self):
        engine = SignatureEngine(["cmd", "powershell"])
        payload = "cmd.exe /c powershell -exec bypass"
        res = engine.detect(payload)
        self.assertTrue(res["detected"])
        self.assertIn("cmd", res["matched_signatures"])
        self.assertIn("powershell", res["matched_signatures"])

    def test_no_match(self):
        engine = SignatureEngine(["cmd", "powershell"])
        payload = "whoami"
        res = engine.detect(payload)
        self.assertFalse(res["detected"])
        self.assertEqual([], res["matched_signatures"])


if __name__ == "__main__":
    unittest.main()