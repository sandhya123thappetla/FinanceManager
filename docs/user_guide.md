# Personal Finance Manager – Documentation

## Project Overview
The Personal Finance Manager is a command-line Python application designed to help users track daily expenses, store financial data, and generate reports. 

Goals:
- Practice Python programming and OOP concepts
- Implement file handling using CSV
- Build a modular and structured application
- Provide an easy menu-based user interface

## Setup Instructions

1. Install Python (3.x)
2. Install VS Code (optional)
3. Clone the repository:

git clone https://github.com/sandhya123thappetla/FinanceManager.git

4. Navigate into project folder:

cd FinanceManager

5. Run the application:

python main.py

## User Manual

Main Menu Options:

1. Add New Expense
   - Enter amount
   - Enter category
   - Enter date
   - Enter description

2. View Expenses
   - Displays all saved expenses

3. Generate Report
   - Shows total and category-wise summary

4. Exit
   - Closes the application

## Code Structure

main.py
Entry point that starts the program.

expense.py
Defines Expense class and attributes.

file_manager.py
Handles reading and writing CSV files.

menu.py
Controls user interface and menu navigation.

reports.py
Generates financial summaries.

utils.py
Contains validation and helper functions.

## Technical Details

Data Structures:
- Lists used to store expenses
- Dictionaries used for category summary

Architecture:
- Modular structure using separate Python files
- Object-Oriented design using Expense class

Algorithms:
- Iteration used for calculating totals
- Filtering used for category reports

## Screenshots

Screenshots available in screenshots/ folder:

- menu.png
- add_expense.png
- report.png

## Testing Evidence

Test Case 1:
Input: Valid expense
Result: Expense saved successfully.

Test Case 2:
Input: Invalid amount
Result: Error message displayed.

Test Case 3:
Generate report
Result: Correct total and category summary shown.

