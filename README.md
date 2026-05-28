# Stock Portfolio Tracker

## Overview

The Stock Portfolio Tracker is a simple Python application developed to calculate and manage stock investments.
This project allows users to enter stock symbols and quantities, calculates the total investment value using predefined stock prices, and optionally saves the portfolio report to a text file.

The project is designed to demonstrate core Python programming concepts in a practical and beginner-friendly way.

---

## Features

* Accepts user input for stock symbols and quantities
* Uses a predefined dictionary to store stock prices
* Calculates individual stock investment values
* Displays total portfolio investment
* Saves portfolio details into a `.txt` report file
* Handles invalid stock entries gracefully

---

## Technologies Used

* Python 3

---

## Python Concepts Applied

* Dictionary
* User Input / Output
* Loops
* Conditional Statements
* Arithmetic Operations
* File Handling

---

## Predefined Stock Prices

| Stock Symbol | Price ($) |
| ------------ | --------- |
| AAPL         | 180       |
| TSLA         | 250       |
| GOOGL        | 135       |
| AMZN         | 145       |
| MSFT         | 330       |

---

## Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py
├── portfolio_report.txt
└── README.md
```

---

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <repository-link>
```

### Step 2: Open the Project in VS Code

Open the project folder using Visual Studio Code.

### Step 3: Run the Python File

Open terminal and execute:

```bash
python stock_portfolio_tracker.py
```

---

## Sample Output

```text
========== STOCK PORTFOLIO TRACKER ==========

How many stocks do you want to add? : 2

Stock Entry 1
Enter stock symbol: AAPL
Enter quantity: 5

Stock Entry 2
Enter stock symbol: TSLA
Enter quantity: 2

========== PORTFOLIO SUMMARY ==========

Stock       : AAPL
Price       : $180
Quantity    : 5
Investment  : $900
----------------------------------------

Stock       : TSLA
Price       : $250
Quantity    : 2
Investment  : $500
----------------------------------------

Total Investment Value : $1400
```

---

## File Saving Feature

After displaying the portfolio summary, the program asks whether the user wants to save the report.

If the user selects `yes`, a file named:

```text
portfolio_report.txt
```

is automatically created in the project folder.

---

## Learning Outcome

By building this project, you can understand:

* How dictionaries work in Python
* How to take and process user input
* How arithmetic operations are used in real-world applications
* How to handle files in Python
* How to organize and display structured data

---

## Future Improvements

* Add live stock price integration using APIs
* Export reports to CSV format
* Add profit/loss analysis
* Build a graphical user interface (GUI)
* Store portfolio history in a database

---

## Author

Developed as part of an internship task to practice Python fundamentals and project development.
