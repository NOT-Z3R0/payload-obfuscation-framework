# Payload Encoding and Obfuscation Framework

## Project Title

Payload Encoding and Obfuscation Framework

## Description

This project implements a practical payload encoding and obfuscation framework used to study how offensive payloads can be transformed to evade simple signature-based detection. Security tools such as antivirus, EDR, IPS, and firewalls often rely on pattern matching, making unmodified payloads easy to identify.  

The framework allows controlled and ethical encoding/obfuscation of test payloads in a lab environment. It supports:

- Encoding: Base64, XOR, ROT13  
- String obfuscation techniques  
- Evasion testing against basic static detection  
- Reporting of original vs. obfuscated payloads and bypass effectiveness  

This helps demonstrate how detection systems rely on patterns, how attackers can bypass simple filters, and why layered security is necessary.

## Features

- **Encoding Module**
  - Base64 encoding & decoding  
  - XOR encryption/encoding with a user-defined key  
  - ROT13 substitution cipher  

- **String Obfuscation Module**
  - Random character insertion  
  - Character splitting & concatenation  
  - Reversible transformations (e.g., text reversal)  
  - Escape-sequence obfuscation  

- **Evasion Testing Module**
  - Simulated signature checks using keyword/pattern matching  
  - Comparison of original vs. obfuscated payloads  
  - Measurement of detection success/failure and bypass rate  

- **Reporting Engine**
  - Lists encoded/obfuscated outputs  
  - Shows behavior comparison between original and modified payloads  
  - Provides practical evasion insights (bypass count and rate)  

- **CLI Interface**
  - Simple command-line usage with `--payload`, `--signatures`, and `--xor-key` options  
  - Results saved to `results/evasion_results.json` for further analysis  

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NOT-Z3R0/payload-obfuscation-framework.git
   cd payload-obfuscation-framework
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # On Linux/macOS:
   source .venv/bin/activate
   # On Windows (PowerShell):
   .venv\Scripts\activate
   ```

3. No external dependencies are required; the project uses only the Python standard library.

## Usage

Basic example:

```bash
python -m src.cli --payload "cmd.exe /c powershell -exec bypass" --signatures cmd powershell exec eval
```

Custom XOR key and different signatures:

```bash
python -m src.cli --payload "whoami" --signatures cmd shell --xor-key mykey123
```

The tool will:

- Show whether the original payload is detected by the given signatures  
- Apply each encoding and obfuscation technique  
- Show detection results for each technique and whether a bypass was achieved  
- Print a summary report with bypass statistics  
- Save detailed results to `results/evasion_results.json`

To run basic tests:

```bash
python -m unittest tests.test_framework
```

## Ethics and legal notice

This framework is intended **only for ethical, educational, and lab-based use** to understand evasion techniques and improve defensive detection rules.  

- Do **not** use this tool against real systems, networks, or applications without explicit permission.  
- Do **not** use this tool for any malicious or illegal activity.  
- The author is not responsible for any misuse of this project.  

Use responsibly and in compliance with all applicable laws and institutional policies.