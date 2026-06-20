# supercleaner.ai
AI Data Cleaning Agent

An AI-powered data cleaning tool that automatically processes Excel and CSV datasets, removes duplicates, handles missing values, and generates intelligent data quality recommendations using Large Language Models (LLMs).

Features

- Supports CSV and Excel files
- Automatic duplicate removal
- Missing value detection and handling
- AI-powered data quality analysis
- Intelligent cleaning recommendations
- Data validation and error detection
- Generates cleaned datasets automatically
- Exports AI-generated cleaning reports
- Easy to use and beginner-friendly

Technologies Used

- Python
- Pandas
- OpenAI API
- OpenAI GPT Models

Installation

Clone the repository:

git clone https://github.com/yourusername/ai-data-cleaning-agent.git
cd ai-data-cleaning-agent

Install dependencies:

pip install pandas openpyxl openai

Project Structure

AI-Data-Cleaning-Agent/
│
├── ai_data_cleaning_agent.py
├── README.md
├── requirements.txt
├── LICENSE
│
├── data.xlsx
├── cleaned_data.xlsx
├── cleaning_report.txt

Usage

1. Add your dataset file:

FILE_PATH = "data.xlsx"

2. Add your API Key:

API_KEY = "YOUR_API_KEY"

3. Run the script:

python ai_data_cleaning_agent.py

Output

The tool automatically generates:

Cleaned Dataset

- cleaned_data.xlsx

AI Cleaning Report

- cleaning_report.txt

The report includes:

- Data Quality Issues
- Missing Value Analysis
- Duplicate Record Analysis
- Data Standardization Suggestions
- Potential Errors
- Final Recommendations

Example Use Cases

- Business Analytics
- Financial Data Cleaning
- Student Database Management
- HR Data Processing
- Survey Data Cleaning
- Customer Data Validation
- Research Dataset Preparation

requirements.txt

pandas
openpyxl
openai

Future Improvements

- Multi-sheet Excel support
- PDF report generation
- Interactive dashboard
- Automatic anomaly detection
- Data visualization integration
- Support for JSON and SQL databases

License

This project is licensed under the MIT License.

Author

Rachit Kumar

BCA Student | Cybersecurity Enthusiast | Python Developer

If you find this project useful, consider giving it a ⭐ on GitHub.