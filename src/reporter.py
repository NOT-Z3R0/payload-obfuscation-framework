"""
Reporting engine:
- Generates human-readable report of original vs obfuscated detection.
- Summarizes bypass effectiveness.
"""

from typing import List, Dict, Any


def generate_report(results: List[Dict[str, Any]]) -> str:
    lines = []
    lines.append("Payload Encoding & Obfuscation Framework - Evasion Report")
    lines.append("=" * 70)

    for i, r in enumerate(results, 1):
        lines.append(f"\n[Result {i}]")
        lines.append(f"Technique: {r['technique']}")
        lines.append(f"Original detected: {r['original_detected']} (signatures: {r['original_sigs']})")
        lines.append(f"Obfuscated detected: {r['obfuscated_detected']} (signatures: {r['obfuscated_sigs']})")
        lines.append(f"Bypass achieved: {r['bypass']}")
        if r.get("note"):
            lines.append(f"Note: {r['note']}")

    lines.append("\nInsights:")
    bypass_count = sum(1 for r in results if r["bypass"])
    lines.append(f"- Total techniques tested: {len(results)}")
    lines.append(f"- Techniques that bypassed all signatures: {bypass_count}")
    if results:
        rate = bypass_count / len(results) * 100
        lines.append(f"- Bypass rate: {rate:.1f}%")

    return "\n".join(lines)