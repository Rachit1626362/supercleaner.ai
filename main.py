import pandas as pd
from openai import OpenAI

# ==========================
# CONFIGURATION
# ==========================
API_KEY = "YOUR_API_KEY"
FILE_PATH = "data.xlsx"

client = OpenAI(api_key=API_KEY)

# ==========================
# LOAD DATA
# ==========================
if FILE_PATH.endswith(".csv"):
    df = pd.read_csv(FILE_PATH)
elif FILE_PATH.endswith((".xlsx", ".xls")):
    df = pd.read_excel(FILE_PATH)
else:
    raise ValueError("Unsupported file format")

print("Dataset Loaded Successfully")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# ==========================
# DATA CLEANING
# ==========================

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        df[col] = df[col].fillna(df[col].median())

# ==========================
# AI ANALYSIS
# ==========================
sample_data = df.head(20).to_string()

prompt = f"""
You are an expert Data Cleaning Agent.

Analyze this dataset sample and provide:

1. Data Quality Issues
2. Data Cleaning Suggestions
3. Column Standardization Suggestions
4. Potential Data Errors
5. Final Recommendations

Dataset:
{sample_data}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a professional data cleaning expert."},
        {"role": "user", "content": prompt}
    ]
)

report = response.choices[0].message.content

# ==========================
# SAVE OUTPUT
# ==========================
df.to_excel("cleaned_data.xlsx", index=False)

with open("cleaning_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("\nCleaning Complete!")
print("Cleaned file saved as cleaned_data.xlsx")
print("AI Report saved as cleaning_report.txt")