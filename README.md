# NeuralRE 🧠🔍

### _AI-Powered Binary Analysis for Security Researchers_

NeuralRE is a specialized automation framework that bridges the gap between traditional static analysis and Large Language Models (LLMs). By leveraging **radare2** for deep binary inspection and **Local LLMs** for contextual reasoning, NeuralRE automates the most time-consuming parts of reverse engineering: function summarization, obfuscation detection, and vulnerability triaging.

## 🚀 The Core Innovation

Traditional reverse engineering requires hours of manual stack analysis and control-flow tracing. NeuralRE introduces an "AI-Augmented Triage" layer. It extracts assembly context via `r2pipe`, normalizes it into Jinja2-structured prompts, and uses local inference (Ollama) to provide a "human-readable" blueprint of unknown binaries.

## ✨ Key Features

- **📊 Context-Aware Function Analysis:** Goes beyond simple disassembly to explain the _logic_ of a function (e.g., "This is a custom base64 decoder with a non-standard alphabet").
    
- **🔒 Heuristic Obfuscation Detection:** Specifically tuned to identify XOR-decryption loops, anti-debugging tricks, and string-stacking techniques common in malware.
    
- **🚨 Automated Vulnerability Scanning:** Scans for high-risk syscalls and unsafe C library usage (e.g., `gets`, `strcpy`, `printf` format string vulnerabilities) with AI-ranked confidence scores.
    
- **📝 Automated Reporting:** Generates structured JSON or Markdown reports for documentation during CTFs or malware incidents.
    

## 🏗️ Technical Architecture

```
┌─────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│   radare2 Core  │      │ Logic Engine     │      │ Local LLM        │
│   (via r2pipe)  │────▶ │ (Python/Jinja2)  │────▶ │ (Ollama/Llama3)  │
└─────────────────┘      └──────────────────┘      └──────────────────┘
        │                         │                         │
  - Disassembly             - Prompt Template         - Behavioral Anal.
  - String Extraction       - Context Trimming        - Vuln Detection
  - CFG Mapping             - JSON Formatting         - Summarization
```

## 🛠️ Security & Privacy Analysis (Critical for Researchers)

Unlike web-based AI tools, NeuralRE is designed for **privacy-first analysis**:

1. **Air-Gapped Operation:** Supports 100% local inference via Ollama. No binary metadata or proprietary code ever leaves your machine.
    
2. **Prompt Engineering Security:** Implements strict system prompts to prevent LLM "hallucinations" regarding assembly instructions.
    
3. **Data Truncation:** Automatically handles large binaries by chunking function data, ensuring the LLM context window isn't overwhelmed.
    

## 🎯 Implementation Details

- **Disassembly Engine:** Radare2 (The industry-standard open-source RE framework).
    
- **Communication Layer:** `r2pipe` provides the Python bridge for seamless binary interaction.
    
- **Inference Engine:** Ollama (defaulting to `phi3` for speed or `llama3` for accuracy).
    
- **Prompt Management:** Jinja2 templates allow for dynamic "persona" switching (e.g., switching from "Malware Analyst" to "Vulnerability Researcher").
    

## 📖 Usage Examples

### 1. Triage a suspicious binary

```
python cli.py analyze suspicious.exe --mode obfuscation --all-functions
```

### 2. Explain a complex assembly function

```
python cli.py analyze challenge.bin --function sym.decrypt_payload --mode explain
```

_Developed by [Your Name] for the security research community._
