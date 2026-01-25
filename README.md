# 💰 Personal Finance Tracker CLI

A command-line personal finance tracker built using **Python** that allows users to record income and expenses, calculate balances, and analyze spending patterns.

This project is designed to practice **Python fundamentals**, **Object-Oriented Programming (OOP)**, and building a **realistic, extensible CLI application** similar to real-world financial tools.

---

## 🚀 Features

- Add income transactions  
- Add expense transactions  
- View current balance (income − expenses)  
- View expenses grouped by category  
- View complete transaction history  
- Interactive, menu-driven CLI  
- Safe numeric input handling  

---

## 🧠 Concepts & Skills Used

- Python classes and objects  
- Object-Oriented Programming (OOP)  
- Encapsulation & separation of concerns  
- Lists and dictionaries  
- Loops and conditional logic  
- User input handling & validation  
- Data aggregation and reporting  
- CLI application design  

---

## 🏗️ Architecture Overview

The application follows a clean separation of responsibilities:

### Transaction
Represents a single financial record (income or expense).

Stores:
- amount (float)
- transaction type (`income` / `expense`)
- category (e.g. food, rent, salary)
- description (free text)

This class is **data-only** — no calculations.

---

### Account
Acts as the **core business logic layer**.

Responsibilities:
- Store all transactions
- Calculate:
  - Total income
  - Total expenses
  - Current balance
  - Expenses grouped by category

All calculations and aggregation live here.

---

### CLI Application
Handles all user interaction.

Responsibilities:
- Display menu options
- Collect user input
- Create `Transaction` objects
- Delegate logic to the `Account` class
- Display formatted output

The CLI performs **no calculations itself**.

---

## 🔁 Data Flow

```
User Input
   ↓
CLI creates Transaction
   ↓
Account stores Transaction
   ↓
Account calculates totals & reports
   ↓
CLI displays results
```

The `Account` object is the **single source of truth** for all financial data.

---

## ▶️ How to Run

Make sure Python 3 is installed.

```bash
python3 finance_tracker.py
```

Follow the on-screen menu to:
- Add income or expenses
- View balance
- Review spending by category
- View full transaction history

---

## 📌 Example Use Cases

- Track daily or monthly expenses  
- Understand spending habits by category  
- Compare income vs expenses  
- Practice building structured Python CLI applications  

---

## 🔮 Planned Improvements

- Save and load data using JSON  
- Add timestamps to transactions  
- Monthly and yearly summaries  
- Export reports to CSV  
- Unit tests  
- Web-based interface in the future  

---

## 🧑‍💻 Author

Built as part of a hands-on Python learning journey by **Vishal Dsouza**  
Focused on writing **clean, readable, and extensible code**.
