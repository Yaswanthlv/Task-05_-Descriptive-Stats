import pandas as pd
import os

# Load the dataset
df = pd.read_csv("data/2019.csv")

# Clean column names
df.columns = [col.strip() for col in df.columns]

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Start building output
output_lines = []

# ===== DESCRIPTIVE STATISTICS =====
output_lines.append("===== DESCRIPTIVE STATISTICS =====\n")
desc = df.describe()
output_lines.append(desc.to_string())
output_lines.append("\n\n")

# ===== BASIC STATISTICS =====
output_lines.append("===== BASIC STATISTICS =====\n")
output_lines.append(f"Number of countries: {df.shape[0]}\n")
output_lines.append(f"Average Happiness Score: {df['Score'].mean():.3f}\n")
max_country = df.loc[df['Score'].idxmax()]
output_lines.append(f"Happiest Country: {max_country['Country or region']} ({max_country['Score']})\n")
min_country = df.loc[df['Score'].idxmin()]
output_lines.append(f"Least Happy Country: {min_country['Country or region']} ({min_country['Score']})\n\n")

# ===== ADVANCED STATISTICS =====
output_lines.append("===== ADVANCED STATISTICS =====\n")

# Correlation with Happiness Score
output_lines.append("Correlation with Happiness Score:\n")
correlation = df.select_dtypes(include='number').corr()
corr_with_score = correlation['Score'].drop('Score').sort_values(ascending=False)
output_lines.extend([f"{k}: {v:.3f}\n" for k, v in corr_with_score.items()])
output_lines.append("\n")

# Top 5 countries by GDP per capita
output_lines.append("Top 5 countries by GDP per capita:\n")
top_gdp = df[['Country or region', 'GDP per capita']].sort_values(by='GDP per capita', ascending=False).head(5)
output_lines.extend([f"{row['Country or region']}: {row['GDP per capita']:.3f}\n" for _, row in top_gdp.iterrows()])
output_lines.append("\n")

# ===== COMPLEX STATISTICS =====
output_lines.append("===== COMPLEX STATISTICS =====\n")

# Normalize all key columns and rank best overall country
key_cols = [
    'GDP per capita', 'Social support', 'Healthy life expectancy',
    'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'
]

# Normalize using Min-Max scaling
normalized_df = df.copy()
for col in key_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    normalized_df[col + ' (norm)'] = (df[col] - min_val) / (max_val - min_val)

# Compute weighted score (equal weights)
normalized_df['Overall Score'] = normalized_df[[col + ' (norm)' for col in key_cols]].mean(axis=1)

# Top 5 countries with highest normalized overall score
output_lines.append("Top 5 countries based on normalized weighted factors:\n")
top_overall = normalized_df[['Country or region', 'Overall Score']].sort_values(by='Overall Score', ascending=False).head(5)
output_lines.extend([f"{row['Country or region']}: {row['Overall Score']:.3f}\n" for _, row in top_overall.iterrows()])
output_lines.append("\n")

# Save to output file
with open("outputs/basic_stats.txt", "w") as f:
    f.writelines(output_lines)
