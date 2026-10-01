# NeuralRE

AI-assisted reverse engineering for binary analysis using radare2 and local large language models.

## Overview

NeuralRE is a lightweight reverse engineering workflow that combines static analysis with language-model reasoning to help security researchers triage unfamiliar binaries. The project extracts function metadata and disassembly from a binary, structures the result into prompt-ready context, and submits it to a locally hosted model for analysis.

This is designed to support common reverse engineering tasks such as:

- function summarization
- behavioral interpretation of assembly
- heuristic detection of obfuscation patterns
- vulnerability-oriented review of suspicious code paths
- quick triage of binaries before deeper manual investigation

## Why this project exists

Traditional RE workflows are often slow and manual, especially when analysts must inspect large binaries by hand. NeuralRE sits between the binary analysis layer and the reasoning layer: radare2 provides disassembly and metadata, while a local model helps interpret the extracted context in a more readable and actionable way.

## Architecture

The project is intentionally simple and modular:

- radare2 for binary analysis and disassembly
- r2pipe for Python integration
- Jinja-based prompt templates for structured analysis prompts
- Ollama for local inference
- optional Streamlit interface for interactive use

```text
Binary file
   │
   ▼
radare2 / r2pipe
   │
   ▼
Function and import/string extraction
   │
   ▼
Prompt construction (Jinja2)
   │
   ▼
Local LLM (Ollama)
   │
   ▼
Analyst-facing summary / triage output
```

## Key capabilities

- Function-level analysis using extracted disassembly and metadata
- Full-binary triage through a disassembly pass
- Support for analysis modes including:
  - summarize
  - obfuscation
  - vuln_analysis
- Local execution to keep analysis on the host machine
- Streamlit-based GUI for easier interactive analysis

## Repository structure

```text
.
├── app/                  # Streamlit interface
├── core/                 # Prompt and analysis orchestration
├── llm/                  # LLM adapters
├── prompts/              # Jinja templates for analysis modes
├── static_analysis/      # radare2 extraction pipeline
├── cli.py                # command-line entry point
├── data_prep.py          # data preparation utilities
├── build.sh              # system setup helper
├── requirements.txt      # Python dependencies
├── README.md             # project documentation
└── bin_samples/         # sample binaries / artifacts
```

## Requirements

Before running NeuralRE, ensure the following are available:

- Python 3.10 or newer
- radare2
- Ollama
- pip for Python package installation

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd neuralre
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install radare2 if it is not already available on the system.

On Arch-based systems, the project includes a helper script:

```bash
./build.sh
```

On Debian/Ubuntu systems, a typical install is:

```bash
sudo apt-get install radare2
```

4. Start Ollama locally and pull a model, for example:

```bash
ollama serve
ollama pull phi3
```

## Usage

The CLI entry point is `cli.py`.

### Analyze a full binary

```bash
python cli.py --binary /path/to/binary --mode summarize --full
```

### Analyze a specific function

```bash
python cli.py --binary /path/to/binary --function 0 --mode obfuscation
```

You can also pass a function address in hexadecimal form:

```bash
python cli.py --binary /path/to/binary --function 0x401000 --mode vuln_analysis
```

### Available modes

- summarize
- obfuscation
- vuln_analysis

### Interactive GUI

A Streamlit UI is available for manual binary upload and analysis:

```bash
streamlit run app/gui.py
```

## Example workflow

1. Identify a suspicious binary.
2. Run the extraction pipeline with radare2.
3. Select a function or analyze the full disassembly.
4. Submit the extracted assembly, imports, and strings to a local model.
5. Review the model output as a triage aid rather than as a replacement for manual reverse engineering.

## Notes and limitations

- The output should be considered an analyst aid, not a definitive security verdict.
- Model quality depends on the prompt structure, binary complexity, and the selected model.
- Large or heavily obfuscated binaries may require targeted analysis on specific functions.
- Local inference is helpful for privacy and control, but performance depends on the host environment.

## License

This project is distributed under the repository license. Please refer to the project files for the applicable terms.

## Intended use

NeuralRE is best suited for research, malware triage, CTF workflows, and exploratory reverse engineering. It is not designed as a black-box autonomous exploit system or a substitute for careful reverse engineering practice.
