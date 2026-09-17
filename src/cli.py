"""
CLI entry point for the framework.
Usage examples:
  python -m src.cli --payload "cmd.exe /c powershell -exec bypass" --signatures cmd powershell exec eval
  python -m src.cli --payload "whoami" --signatures cmd shell --xor-key mykey123
"""

import argparse
import json
from pathlib import Path

from .encoders import encode_base64, encode_rot13_text, xor_bytes
from .obfuscators import (
    obf_random_insertion,
    obf_split_concat,
    obf_escape_sequences,
    obf_reverse_text,
)
from .detector import SignatureEngine
from .reporter import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Payload Encoding & Obfuscation Framework (Lab/Educational Use Only)"
    )
    parser.add_argument(
        "--payload",
        required=True,
        help="Input payload (string). Example: 'cmd.exe /c powershell -exec bypass'"
    )
    parser.add_argument(
        "--signatures",
        nargs="+",
        default=["cmd", "powershell", "shell", "exec", "eval"],
        help="Signature keywords to test against"
    )
    parser.add_argument(
        "--xor-key",
        default="secretkey",
        help="XOR key (string)"
    )
    args = parser.parse_args()

    payload_text = args.payload
    payload_bytes = payload_text.encode("utf-8")
    xor_key = args.xor_key.encode("utf-8")

    engine = SignatureEngine(args.signatures)

    # Define techniques: name + transform function (bytes -> str for display)
    techniques = [
        ("base64", lambda b: encode_base64(b).decode("ascii")),
        ("rot13_text", lambda b: encode_rot13_text(b.decode("utf-8", errors="replace"))),
        ("xor_hex", lambda b: xor_bytes(b, xor_key).hex()),
        ("random_insertion", lambda b: obf_random_insertion(b.decode("utf-8", errors="replace"))),
        ("split_concat", lambda b: obf_split_concat(b.decode("utf-8", errors="replace"))),
        ("escape_sequences", lambda b: obf_escape_sequences(b.decode("utf-8", errors="replace"))),
        ("reverse", lambda b: obf_reverse_text(b.decode("utf-8", errors="replace"))),
    ]

    results = []

    print("=== Payload Encoding & Obfuscation Framework ===")
    print(f"Original payload: {payload_text}")
    orig_det = engine.detect(payload_text)
    print(f"Original detection: detected={orig_det['detected']}, signatures={orig_det['matched_signatures']}")
    print()

    for name, transform in techniques:
        try:
            obf_payload = transform(payload_bytes)
            obf_det = engine.detect(obf_payload)

            # Bypass = originally detected, now not detected
            bypass = orig_det["detected"] and not obf_det["detected"]

            results.append({
                "technique": name,
                "original_detected": orig_det["detected"],
                "original_sigs": orig_det["matched_signatures"],
                "obfuscated_detected": obf_det["detected"],
                "obfuscated_sigs": obf_det["matched_signatures"],
                "bypass": bypass,
                "obfuscated_payload_sample": obf_payload[:120] + ("..." if len(obf_payload) > 120 else ""),
                "note": ""
            })

            print(f"[{name}]")
            print(f"Obfuscated (sample): {obf_payload[:160]}")
            print(f"Detection: detected={obf_det['detected']}, signatures={obf_det['matched_signatures']}, bypass={bypass}")
            print()

        except Exception as e:
            print(f"[{name}] ERROR: {e}")
            print()

    report = generate_report(results)
    print(report)

    # Save JSON results in results/ folder
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    output_file = results_dir / "evasion_results.json"

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "original_payload": payload_text,
                "signatures_used": args.signatures,
                "original_detection": orig_det,
                "results": results
            },
            f,
            indent=2
        )

    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()