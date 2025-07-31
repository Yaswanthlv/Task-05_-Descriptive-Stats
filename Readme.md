# 📊 Task 05 – Descriptive Statistics & LLM Evaluation

**Dataset**: [World Happiness Report 2019 (Kaggle)](https://www.kaggle.com/datasets/unsdsn/world-happiness)

---

## 🧠 Task Overview

This task focuses on analyzing the **World Happiness Report 2019** using statistical methods and evaluating the performance of a **Large Language Model (LLM)** in interpreting real-world data.

The task involves:

- Generating **descriptive, basic, advanced, and complex statistics** using Python and Pandas.
- Forming **natural language questions** about the dataset.
- Recording LLM-generated answers to those questions.
- Writing a script to compute the **actual, factual answers** from the dataset.
- Comparing and **evaluating** the LLM responses based on accuracy.

---

## 🗂 Repository Structure

```
├── data/
│ └── 2019.csv # Dataset file (excluded via .gitignore)
├── outputs/
│ ├── basic_stats.txt # Summary statistics output
│ └── factual_answers.json # Script-generated factual answers
├── .gitignore # To exclude data and output files from Git
├── basic_stats.py # Script to generate descriptive and advanced statistics
├── generate_factual_answers.py # Script to compute correct answers for all questions
├── fill_correct_answers.py # Script to inject correct answers into llm_questions.md
├── llm_questions.md # LLM prompts, responses, correct answers, and evaluations
└── README.md # Project documentation

```
---

## ⚙️ How to Run

1. Place the dataset file as `data/2019.csv`  
   (Download from [here](https://www.kaggle.com/datasets/unsdsn/world-happiness))

2. Run the script to generate descriptive and advanced statistics:  
   python basic_stats.py

3. Generate factual answers from the dataset:  
   python generate_factual_answers.py

4. Inject factual answers into the markdown file:  
   python fill_correct_answers.py

---

## 🔍 Evaluation Strategy

The evaluation of LLM responses was done manually based on the following criteria:

- **Accuracy**: Does the LLM's response match the true statistical result?
- **Reasoning**: Does it provide a correct explanation or justification?
- **Format**: Are units, thresholds, and values correctly interpreted?

Each evaluation is recorded in `llm_questions.md` under the **Evaluation** section.

---


## 📊 LLM Evaluation Summary

Out of **16 total questions**:

- ✅ **14 answers were fully correct**  
- ⚠️ **1 answer was partially correct** (Q15 – missed a few additional outlier countries)  
- ❌ **1 answer was incorrect** (Q13 – stated a wrong threshold for social support)

Overall, the LLM demonstrated **high accuracy** and **strong reasoning skills**, especially on straightforward statistical queries.


---


## 📈 Skills Practiced

- Python scripting and automation  
- Data analysis with Pandas  
- Correlation and statistical ranking  
- Normalization and scoring logic  
- Evaluating AI/LLM outputs against factual computation  
- Reproducible research and documentation  


---
## ✅ Summary of Activity

I explored descriptive and advanced statistical concepts using the World Happiness Report 2019. I created Python scripts to answer complex questions, evaluated an LLM's output against these factual answers, and reflected on both human and AI-based interpretation of data.
