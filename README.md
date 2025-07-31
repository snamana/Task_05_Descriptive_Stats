# Task_05_Descriptive_Stats

This repository contains scripts and prompt logs used to evaluate the reasoning performance of Large Language Models (LLMs) such as ChatGPT on Syracuse University Men’s Basketball 2024–25 season data. The goal is to assess whether the LLM can correctly answer natural language questions derived from a real-world sports dataset when guided through structured prompt engineering.

---

## Dataset

- **Title**: Syracuse University Men’s Basketball 2024–25 Season Stats  
- **Source**: [https://cuse.com/sports/mens-basketball/stats/2024-25](https://cuse.com/sports/mens-basketball/stats/2024-25)  

---

## Files

| File/Folder              | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `scripts.py` | Python script with small simulations to validate LLM answers manually         |
| `prompts.md`            | Log of all natural language questions asked, LLM responses, and evaluations   |
| `report.md`       | Narrative summary of what worked, what didn’t, and how LLMs handled reasoning |
| `README.md`                        | This file – repository overview and usage instructions                        |

---

## Instructions

1. **Run helper validation scripts** (optional)
   ```bash
   python3 scripts/scripts.py

## Summary of Findings
- Basic factual questions (e.g., total games, top scorer) were answered correctly by the LLM.

- Judgment-based or improvement questions needed engineered metrics (e.g., comparing player PPG in first vs. last 5 games).

- Prompt engineering played a crucial role — supplying structured context (like tables or metrics) significantly improved answer quality.

- LLMs failed or gave generic responses when asked strategic or speculative questions without guidance.

- When treated like an assistant coach (i.e., prompted with specific data), the LLM offered meaningful insights.
 
