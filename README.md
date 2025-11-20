# Financial Transactions Summary Tool

# Project Overview
This project processes a financial transactions dataset and produces clean summaries and visual insights. It was developed collaboratively using Agile practices, including user stories, sprint planning, and a branch-per-feature workflow.

#  Sprint Goal
Deliver a working Python tool that loads data, cleans it, generates summaries, visualizations, and passes test cases while following Agile collaboration standards.

## Project Structure
financial-transactions-summary-tool/
│
├── main.py
├── requirements.txt
├── financial_transactions.csv
│
└── src/
├── load_data.py
├── summary_functions.py
├── reports.py
│
└── tests/
└── test_transactions.py

## Features

- Reads the raw CSV file
- Removes invalid or missing records
- Standardizes column formats for consistency

- Monthly credit/debit trend line chart  
- Income vs. expense pie chart  
- Top 10 customers bar chart  
- Top 5 transactions bar chart

## User Stories (Sprint Planning)

## Tests
Run tests: pytest

### US-01 Implementation

This user story involved building the core data-loading step for the project. The team implemented the load_and_clean_data() function, which reads the raw CSV file, removes missing or invalid records, standardizes data types, and prepares a clean dataset for all other summaries and visualizations. This ensures that every feature in the tool is based on accurate and reliable data.

### US-02 Income & Expense Summary
For this project, I completed User Story 2, which focused on calculating the total income and total expenses from the financial transactions dataset. My work involved writing the calculate_income_expense() function inside summary_functions.py. This function filters the transactions into credit (income) and debit (expenses), calculates the totals, and returns the values so they can be displayed in the main program.

I also verified the correctness of the calculations by checking the results directly against the dataset and ensured that the function integrated smoothly into main.py.

This contribution allowed the team to generate a clear financial summary that shows the overall financial position of the user.

## Links 

GitHub Repository: https://github.com/barishettynaveen/Financial-transaction-summary-tool-Sec-7-Group-5

Taiga Project: https://tree.taiga.io/project/prasannapodhem-sketch-financial-transactions-summary-tool
















