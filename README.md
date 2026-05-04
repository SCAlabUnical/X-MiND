# X-MiND

**X-MiND** is an explainable framework for detecting **mental-status shifts** in timestamped user digital traces, such as social media posts, chats, and online interactions.

The name **X-MiND** stands for **eXplainable Mental-status shift Detection**.

The repository accompanies the paper:

> **Explainable Detection of Mental Status Shifts in User Digital Traces**  
> *Under revision at* **Social Network Analysis and Mining**

## Description

Users generate digital traces that may reflect aspects of their mental state over time. X-MiND organizes these traces into temporal trajectories and analyzes them to identify phases of improvement, deterioration, or stability.

The framework combines:

- BERT-based models for extracting signals such as sentiment, emotion, and depression severity;
- temporal aggregation to build user-level trajectories;
- change-point detection to identify meaningful mental-status shifts;
- large language models to generate concise and human-readable reports.

X-MiND is intended for research purposes and does **not** aim to provide clinical diagnosis.

## Pipeline

```text
Digital traces
   ↓
BERT-based signal extraction
   ↓
Temporal trajectory construction
   ↓
Change-point detection
   ↓
LLM-based explainable report
```

## Installation

```bash
git clone https://github.com/<username>/X-MiND.git
cd X-MiND
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py --input data/sample_data.csv --output results/
```

Please adapt the command according to the final repository structure.

## Input Format

A minimal input file should contain timestamped user texts:

```text
user_id,timestamp,text
```

## Citation

If you use this repository, please cite:

```bibtex
@article{marozzo2026xmind,
  title   = {Explainable Detection of Mental Status Shifts in User Digital Traces},
  author  = {Marozzo, Fabrizio and others},
  journal = {Social Network Analysis and Mining},
  year    = {2026},
  note    = {Under revision}
}
```

Please update the citation with the final bibliographic details once the paper is accepted.

## Contact

**Fabrizio Marozzo**  
University of Calabria  
Email: fabrizio.marozzo@unical.it
