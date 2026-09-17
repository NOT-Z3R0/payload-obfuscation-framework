# Payload Encoding & Obfuscation Framework

Educational lab project to study how offensive payloads can be transformed to evade simple signature-based detection.  
This project is for **ethical, lab-only use** to understand evasion techniques and improve defensive detection.

## Features

- **Encoding Module**
  - Base64 encoding & decoding
  - XOR encryption/encoding with user-defined key
  - ROT13 substitution cipher

- **String Obfuscation Module**
  - Random character insertion
  - Character splitting & concatenation
  - Reversible transformations (reverse)
  - Escape-sequence obfuscation

- **Evasion Testing Module**
  - Simulated signature checks using keyword/pattern matching
  - Comparison of original vs obfuscated payloads
  - Detection success/failure measurement

- **Reporting Engine**
  - Lists encoded/obfuscated outputs
  - Behavior comparison between original and modified payloads
  - Practical evasion insights (bypass rate, techniques)

## Requirements

- Python 3.8+
- No external dependencies (standard library only)

## Installation

```bash
git clone https://github.com/NOT-Z3R0/payload-obfuscation-framework 
cd payload-obfuscation-framework
```

(Optional) Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Usage

Basic example:

```bash
python -m src.cli --payload "cmd.exe /c powershell -exec bypass" --signatures cmd powershell exec eval
```

Custom XOR key:

```bash
python -m src.cli --payload "whoami" --signatures cmd shell --xor-key mykey123
```

Results (including detection status and bypass info) are saved to:

```text
results/evasion_results.json
```

## Project Structure

- `src/encoders.py` – Base64, XOR, ROT13 implementations  
- `src/obfuscators.py` – String obfuscation techniques  
- `src/detector.py` – Signature engine for evasion testing  
- `src/reporter.py` – Report generation  
- `src/cli.py` – Command-line interface  
- `tests/` – Basic unit tests  

## Learning Outcomes

- How payloads are manipulated for evasion  
- How obfuscation complicates malware detection  
- How red teams hide malicious content  
- How blue teams can strengthen detection rules  
- Practical encoding and transformation logic  

## License

Educational use only. Do not use for malicious activities.