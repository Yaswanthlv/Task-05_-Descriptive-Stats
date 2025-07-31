import pandas as pd
import os
import json

# Load the dataset
df = pd.read_csv("data/2019.csv")
df.columns = [col.strip() for col in df.columns]  # Clean column names

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Prepare answers dictionary
answers = {}

# -----------------------------
# SIMPLE QUESTIONS
# -----------------------------

# Q1: Which country has the highest happiness score?
# 👉 We find the row where the 'Score' column has the maximum value
answers["Q1"] = df.loc[df['Score'].idxmax(), 'Country or region']

# Q2: Which country has the lowest happiness score?
# 👉 Same logic as Q1 but using the minimum instead of maximum
answers["Q2"] = df.loc[df['Score'].idxmin(), 'Country or region']

# Q3: How many countries are included in the dataset?
# 👉 Use number of rows in the DataFrame
answers["Q3"] = df.shape[0]

# Q4: What is the average happiness score across all countries?
# 👉 Take the mean of the 'Score' column and round to 3 decimals
answers["Q4"] = round(df['Score'].mean(), 3)

# Q5: Which 5 countries have the highest GDP per capita?
# 👉 Sort the DataFrame by 'GDP per capita' descending and take top 5 rows
top5_gdp = df[['Country or region', 'GDP per capita']]\
    .sort_values(by='GDP per capita', ascending=False).head(5)
answers["Q5"] = top5_gdp.to_dict(orient='records')

# Q6: Which factor is most positively correlated with happiness score?
# 👉 Calculate correlations and find the factor most correlated with 'Score'
correlations = df.corr(numeric_only=True)
answers["Q6"] = correlations['Score'].drop('Score').idxmax()

# Q7: What is the average healthy life expectancy among all countries?
# 👉 Just a mean of 'Healthy life expectancy'
answers["Q7"] = round(df['Healthy life expectancy'].mean(), 3)

# Q8: Which country has the highest generosity score?
# 👉 Locate the row with the max value in 'Generosity'
answers["Q8"] = df.loc[df['Generosity'].idxmax(), 'Country or region']

# -----------------------------
# COMPLEX QUESTIONS
# -----------------------------

# Q9: If a country wants to increase its happiness score by 1 point, which single factor should it invest in first and why?
# 👉 Pick the variable with the highest correlation to 'Score'
sorted_corrs = correlations['Score'].drop('Score').sort_values(ascending=False)
answers["Q9"] = sorted_corrs.idxmax()

# Q10: Rank the six contributing factors by their importance in determining happiness.
# 👉 Just list them in descending order of correlation with 'Score'
answers["Q10"] = sorted_corrs.index.tolist()

# Q11: Which country is the best overall performer when all six factors are normalized and averaged equally?
# 👉 Normalize each of the six columns and compute their average per country
factor_cols = [
    'GDP per capita', 'Social support', 'Healthy life expectancy',
    'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'
]

normalized_df = df.copy()
for col in factor_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    normalized_df[col + ' (norm)'] = (df[col] - min_val) / (max_val - min_val)

# 👉 Compute the overall normalized score as the average of all normalized factor values
normalized_df['Overall Score'] = normalized_df[[col + ' (norm)' for col in factor_cols]].mean(axis=1)
answers["Q11"] = normalized_df.loc[normalized_df['Overall Score'].idxmax(), 'Country or region']

# Q12: Are there any countries that rank high in generosity but have a low happiness score?
# 👉 Filter countries above 90th percentile in generosity and below 25th percentile in score
gen_threshold = df['Generosity'].quantile(0.90)
score_threshold = df['Score'].quantile(0.25)
q12_result = df[(df['Generosity'] > gen_threshold) & (df['Score'] < score_threshold)]
answers["Q12"] = q12_result['Country or region'].tolist()

# Q13: Is there a threshold value of social support above which happiness score tends to exceed 7?
# 👉 Find all countries with 'Social support' > 0.9 and check which of those have 'Score' > 7
support_threshold = 0.9
q13_result = df[(df['Social support'] > support_threshold) & (df['Score'] > 7)]
answers["Q13"] = {
    'Threshold': support_threshold,
    'Countries': q13_result['Country or region'].tolist()
}

# Q14: What patterns can be observed between perceptions of corruption and happiness levels?
# 👉 Just return the correlation value (usually negative)
answers["Q14"] = {
    'Correlation': round(correlations['Score']['Perceptions of corruption'], 3)
}

# Q15: Which countries are outliers – performing better in happiness than their GDP per capita would suggest?
# 👉 Rank both GDP and Score, and find countries where Score rank is much better than GDP rank
df['GDP_rank'] = df['GDP per capita'].rank(ascending=False)
df['Score_rank'] = df['Score'].rank(ascending=False)
df['Rank_diff'] = df['GDP_rank'] - df['Score_rank']
outliers = df[df['Rank_diff'] > 30].sort_values(by='Rank_diff', ascending=False)
answers["Q15"] = outliers['Country or region'].tolist()

# Q16: As a policy advisor, which factor would you recommend improving if the goal is to help countries with low happiness scores catch up with the top 10?
# 👉 Compare average values for each factor between top 10 and bottom 25% countries
top_10 = df.nlargest(10, 'Score')
bottom_25 = df.nsmallest(39, 'Score')  # ~25% of 156 countries
mean_diff = {}
for col in factor_cols:
    mean_diff[col] = top_10[col].mean() - bottom_25[col].mean()

# 👉 Return the factor with the largest average gap
answers["Q16"] = max(mean_diff, key=mean_diff.get)

# -----------------------------
# Save the answers
# -----------------------------
with open("outputs/factual_answers.json", "w") as f:
    json.dump(answers, f, indent=4)

print("✅ factual_answers.json has been saved in /outputs")
