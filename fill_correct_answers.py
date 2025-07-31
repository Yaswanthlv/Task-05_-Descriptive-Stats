import json
from pathlib import Path

# Paths
json_path = Path("outputs/factual_answers.json")
md_file_path = Path("llm_questions.md")

# Load factual answers
with open(json_path, "r") as f:
    answers = json.load(f)

# Load the markdown file (fix encoding issue)
with open(md_file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Inject correct answers in place
updated_lines = []
question_number = 1

for line in lines:
    if line.strip().startswith("**Correct Answer (from script):**"):
        key = f"Q{question_number}"
        answer = answers.get(key, "N/A")

        # Format nicely
        if isinstance(answer, list):
            formatted = ", ".join(map(str, answer))
        elif isinstance(answer, dict):
            formatted = json.dumps(answer, indent=2)
        else:
            formatted = str(answer)

        updated_lines.append(f"**Correct Answer (from script):** {formatted}\n")
        question_number += 1
    else:
        updated_lines.append(line)

# ✅ Overwrite the original file with correct answers
with open(md_file_path, "w", encoding="utf-8") as f:
    f.writelines(updated_lines)

print(f"✅ Correct answers inserted directly into: {md_file_path}")
