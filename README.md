# 🧠 Intelligent Bank Expense Classifier
**Personal automation project using Python + OpenAI**

---

## 📂 Overview
This is a personal Python project developed to automate the classification of bank expenses using natural language processing. It reads an Excel file with bank transactions, processes the data, and classifies each transaction into categories using the OpenAI API. The goal is to facilitate personal financial analysis and generate organized statistics by expense type.

---

## ⚙️ Technologies Used
- Python  
- pandas  
- OpenAI API (gpt-3.5-turbo)  
- dotenv  
- Excel (.xls/.xlsx)

---

## 🔀 Project Structure

The project is divided into **three main modules**, making it easy to reuse and maintain:

### 1. Data Loader
Responsible for reading the Excel file with bank transactions.  
It extracts the relevant columns (date, description, amount, balance, and ID), and renames them to standardized names for consistency across the project.

### 2. Expense Classifier
Uses the OpenAI API to assign a category to each transaction based on its description.  
The list of categories can be customized via environment variables. The function also handles edge cases like empty or malformed descriptions.

### 3. Main Execution Script
Coordinates the entire workflow:
- Loads the Excel file
- Classifies each transaction
- Exports the final result with an additional column for the category

The output is a new Excel file with enriched data, ready for visualization or further processing.

---

## 📁 Folder Structure
```
.
├── files/
│   └── cuenta.xls                # Original bank transaction file
│   └── gastos_clasificados.xlsx # Final classified output
├── classifier.py                # OpenAI classification module
├── data_loader.py              # Excel loading script
├── main.py                     # Main controller script
├── .env                        # Environment variables (API keys and categories)
└── requirements.txt            # Project dependencies
```

## 🌐 Key Features
- ✅ Automatic classification using natural language
- ✅ Customizable categories via environment file
- ✅ Works with real banking data formats
- ✅ Modular, clean and maintainable code

---

## 🔒 Security and Configuration
API keys and category settings are stored securely in a `.env` file, which is not tracked by version control.

Example content:
```
OPENAI_API_KEY=your_api_key
OPENAI_ORG_ID=your_organization_id
PROMPT_CAT=Rent,Groceries,Online Services,Restaurants,...
```

## 📌 Future Improvements
- Add data visualizations using Power BI or matplotlib  
- Offline classification with local machine learning models  
- Duplicate transaction detection  
- Export to other formats (CSV, JSON)  
- Create a simple web interface to upload and view results

---

## 💻 Final Output
The tool generates an Excel file with an additional column called “Category”, showing the classification for each expense.


