"""
Evasion testing module:
- Simulated signature checks using keyword/pattern matching.
- Returns detection status and matched signatures.
"""

from typing import List, Dict, Any


class SignatureEngine:
    """
    Simple signature engine that checks if any signature substring
    appears in the payload (case-insensitive).
    """

    def __init__(self, signatures: List[str]):
        self.signatures = [s.lower() for s in signatures]

    def detect(self, payload: str) -> Dict[str, Any]:
        payload_lower = payload.lower()
        hits = []
        for sig in self.signatures:
            if sig in payload_lower:
                hits.append(sig)
        return {
            "detected": len(hits) > 0,
            "matched_signatures": hits
        }