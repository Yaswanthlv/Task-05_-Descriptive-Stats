# LLM Questions & Evaluation – World Happiness Report 2019

This file contains natural language questions asked to a Large Language Model (LLM) based on the World Happiness Report 2019 dataset. Each question includes a placeholder for the LLM response, the correct answer from actual analysis, and an evaluation. Do not change even a text from other sections

---

## ✅ SIMPLE QUESTIONS

### Question 1:
**Prompt:** Which country has the highest happiness score?  
**LLM Response:**  Finland (Score: 7.769)  
**Correct Answer (from script):** Finland
**Evaluation:** Yes – The LLM correctly identified Finland as the country with the highest happiness score based on the dataset.  

---

### Question 2:
**Prompt:** Which country has the lowest happiness score?  
**LLM Response:**  South Sudan (Score: 2.853)  
**Correct Answer (from script):** South Sudan
**Evaluation:** Yes – The LLM correctly named South Sudan as the least happy country with matching score.  

---

### Question 3:
**Prompt:** How many countries are included in the dataset?  
**LLM Response:**  156  
**Correct Answer (from script):** 156
**Evaluation:** Yes – The LLM's answer matches exactly with the number of rows in the dataset.  

---

### Question 4:
**Prompt:** What is the average happiness score across all countries?  
**LLM Response:**  5.41  
**Correct Answer (from script):** 5.407
**Evaluation:** Yes – The LLM rounded the correct average value slightly, but it is factually accurate and consistent with the data.  

---

### Question 5:
**Prompt:** Which 5 countries have the highest GDP per capita?  
**LLM Response:**  Qatar (1.684)  
Luxembourg (1.609)  
Singapore (1.572)  
United Arab Emirates (1.503)  
Kuwait (1.500)  
**Correct Answer (from script):** {'Country or region': 'Qatar', 'GDP per capita': 1.684}, {'Country or region': 'Luxembourg', 'GDP per capita': 1.609}, {'Country or region': 'Singapore', 'GDP per capita': 1.572}, {'Country or region': 'United Arab Emirates', 'GDP per capita': 1.503}, {'Country or region': 'Kuwait', 'GDP per capita': 1.5}
**Evaluation:** Yes – The countries and their GDP values are accurate and match the dataset ordering precisely.  

---

### Question 6:
**Prompt:** Which factor is most positively correlated with happiness score?  
**LLM Response:**  GDP per capita (Correlation: 0.794)  
**Correct Answer (from script):** GDP per capita
**Evaluation:** Yes – The LLM correctly identified GDP per capita as the most correlated factor, and even provided the correct correlation value.  

---

### Question 7:
**Prompt:** What is the average healthy life expectancy among all countries?  
**LLM Response:**  0.725  
**Correct Answer (from script):** 0.725
**Evaluation:** Yes – The LLM’s answer is perfectly aligned with the factual mean from the dataset.  

---

### Question 8:
**Prompt:** Which country has the highest generosity score?  
**LLM Response:**  Myanmar (Generosity: 0.566)  
**Correct Answer (from script):** Myanmar
**Evaluation:** Yes – Myanmar is correctly identified as the most generous country based on the dataset.  

---

## 🔍 COMPLEX QUESTIONS

### Question 9:
**Prompt:** If a country wants to increase its happiness score by 1 point, which single factor should it invest in first and why?  
**LLM Response:**  If a country wants to increase its happiness score by 1 point, it should first invest in GDP per capita, as it has the highest combined effect (correlation × variability).  
→ Why? It has the strongest positive correlation (0.794) and a wide range across countries, offering high leverage.  
**Correct Answer (from script):** GDP per capita
**Evaluation:** Yes – The LLM correctly chose GDP per capita and justified it using correlation, which aligns with the script.  

---

### Question 10:
**Prompt:** Rank the six contributing factors by their importance in determining happiness.  
**LLM Response:**  GDP per capita — 0.794  
Healthy life expectancy — 0.780  
Social support — 0.777  
Freedom to make life choices — 0.567  
Perceptions of corruption — 0.386  
Generosity — 0.076  
**Correct Answer (from script):** GDP per capita, Healthy life expectancy, Social support, Freedom to make life choices, Perceptions of corruption, Generosity, Overall rank
**Evaluation:** Yes – The LLM listed all six factors in the same order as the correlation-based ranking from the script.  

---

### Question 11:
**Prompt:** Which country is the best overall performer when all six factors are normalized and averaged equally?  
**LLM Response:**  Singapore  
**Correct Answer (from script):** Singapore
**Evaluation:** Yes – Singapore is correctly identified as the highest overall normalized performer.  

---

### Question 12:
**Prompt:** Are there any countries that rank high in generosity but have a low happiness score?  
**LLM Response:**  Myanmar  
Haiti  
Kenya  
Gambia  
Syria  
Comoros  
These countries are generous (top 25%) but have happiness scores in the bottom 25%.  
**Correct Answer (from script):** Kenya, Myanmar, Haiti, Syria
**Evaluation:** Yes – The LLM correctly identified multiple countries from the correct set. The extra countries mentioned do not significantly affect the correctness.  

---

### Question 13:
**Prompt:** Is there a threshold value of social support above which happiness score tends to exceed 7?  
**LLM Response:**  Countries with a happiness score >7 all have social support ≥ 1.441.  
✅ This suggests 1.44 is a strong threshold — below that, it's rare to reach top happiness levels.  
**Correct Answer (from script):** {
  "Threshold": 0.9,
  "Countries": [
    "Finland",
    "Denmark",
    "Norway",
    "Iceland",
    "Netherlands",
    "Switzerland",
    "Sweden",
    "New Zealand",
    "Canada",
    "Austria",
    "Australia",
    "Costa Rica",
    "Israel",
    "Luxembourg",
    "United Kingdom",
    "Ireland"
  ]
}
  "Threshold": 0.9,
  "Countries": [
    "Finland",
    "Denmark",
    "Norway",
    "Iceland",
    "Netherlands",
    "Switzerland",
    "Sweden",
    "New Zealand",
    "Canada",
    "Austria",
    "Australia",
    "Costa Rica",
    "Israel",
    "Luxembourg",
    "United Kingdom",
    "Ireland"
  ]
}  
**Evaluation:** No – The LLM stated a much higher threshold (1.44), which is incorrect. According to the dataset, the actual threshold above which most countries exceed a score of 7 is ~0.9.  

---

### Question 14:
**Prompt:** What patterns can be observed between perceptions of corruption and happiness levels?  
**LLM Response:**  Correlation = +0.386 (moderate positive).  
Interestingly, countries with higher corruption scores (i.e., perceived as less corrupt) tend to have higher happiness, especially in the top quartile.  
**Correct Answer (from script):** {
  "Correlation": 0.386
}
  "Correlation": 0.386
}  
**Evaluation:** Yes – The LLM correctly captured the pattern and cited the right correlation value.  

---

### Question 15:
**Prompt:** Which countries are outliers – performing better in happiness than their GDP per capita would suggest?  
**LLM Response:**  Costa Rica  
Finland  
Somalia  
Guatemala  
Nicaragua  
Denmark  
Uzbekistan  
El Salvador  
Honduras  
Iceland  
✅ These countries are happier than GDP alone would predict, indicating other strong contributing factors like social support or freedom.  
**Correct Answer (from script):** Guatemala, El Salvador, Uzbekistan, Nicaragua, Costa Rica, Honduras, Tajikistan, Pakistan, Somalia, Kosovo, Bolivia, Brazil, Moldova, Jamaica, Ecuador, Niger, Kyrgyzstan, Mexico, Colombia
**Evaluation:** Partially – The LLM captured many valid outliers but missed several others. While not exhaustive, its core interpretation was aligned with the dataset pattern.  

---

### Question 16:
**Prompt:** As a policy advisor, which factor would you recommend improving if the goal is to help countries with low happiness scores catch up with the top 10?  
**LLM Response:** GDP per capita shows the largest gap between top 10 and bottom 20 countries, suggesting it’s the most impactful area for improvement.  
**Correct Answer (from script):** GDP per capita
**Evaluation:** Yes – The LLM’s reasoning aligns with the calculated average differences between top and bottom countries.  

---

**LLM Used:** ChatGPT (GPT-4o)
**Dataset:** World Happiness Report 2019  

