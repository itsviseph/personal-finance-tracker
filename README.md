# 💰 Personal Finance Tracker CLI

A command-line personal finance tracker built using **Python** that allows users to record income, expenses, and recurring subscriptions, calculate balances, and analyze spending patterns.

This project focuses on writing **clean, modular, and production-style Python code**, using proper packages, modules, and separation of concerns—similar to real-world backend systems.

---

## 🚀 Features

### Transactions
- Add income transactions  
- Add expense transactions  
- View complete transaction history  
- Search transactions by category, description, or amount  

### Financial Insights
- View current balance (income − expenses)  
- View expenses grouped by category  
- View adjusted balance (after subscriptions)  

### Subscriptions
- Add recurring subscriptions  
- View all subscriptions  
- Calculate total monthly subscription cost  
- View top subscriptions by cost  

### General
- Interactive, menu-driven CLI  
- Safe numeric input handling  
- Modular, scalable project structure  

---

## 🧠 Concepts & Skills Used

- Python packages & modules  
- Object-Oriented Programming (OOP)  
- Encapsulation & separation of concerns  
- Lists and dictionaries  
- Loops and conditional logic  
- User input handling & validation  
- Data aggregation and reporting  
- Sorting and filtering data  
- CLI application design  
- `__name__ == "__main__"` execution pattern  

---

## 🏗️ Project Structure
```
personal-finance-tracker/
│
├── README.md
├── main.py
└── finance_tracker/
  ├── __init__.py
  ├── models.py
  ├── account.py
  └── cli.py
```

## 📂 File Responsibilities

### `models.py`
Contains **data-only classes**:
- `Transaction`
- `Subscription`

No calculations or user interaction logic.

---

### `account.py`
Acts as the **business logic layer**.

Responsibilities:
- Store transactions and subscriptions
- Calculate:
  - Total income
  - Total expenses
  - Current balance
  - Adjusted balance (after subscriptions)
  - Expenses grouped by category
  - Monthly subscription cost
  - Top subscriptions by cost

This is the **single source of truth** for financial data.

---

### `cli.py`
Handles **all user interaction**.

Responsibilities:
- Display menu options
- Collect and validate user input
- Create `Transaction` and `Subscription` objects
- Call methods on the `Account` class
- Format and display output

The CLI performs **no calculations itself**.

---

### `main.py`
The **application entry point**.

Responsibilities:
- Start the CLI application
- Ensure code only runs when executed directly

Uses the standard Python pattern:
```python
if __name__ == "__main__":
    run()
```
run() is imported from finance_tracker.cli

## 🔁 Data Flow

 ```
User Input  
  ↓  
CLI collects input 
  ↓  
Account stores and processes data  
  ↓  
Account returns calculated or filtered results  
  ↓  
CLI formats and displays output  
```

The `Account` object is the **single source of truth** for all financial data.

---

## ▶️ How to Run

Make sure Python 3 is installed.

From the project root directory:
```bash
python3 main.py
```

Follow the on-screen menu to:
- Add income, expenses, and subscriptions
- View balances and adjusted balances
- Review spending by category
- Analyze subscription costs
- Search transaction history

---

## 📌 Example Use Cases

- Track daily or monthly expenses  
- Monitor recurring subscriptions  
- Understand spending habits by category  
- See how subscriptions affect available balance  
- Practice building structured Python CLI applications  

---

## 🔮 Planned Improvements

- Persist data using JSON (save/load)
- Add timestamps to transactions
- Edit or delete transactions and subscriptions
- Normalize subscription billing cycles to monthly cost
- Monthly and yearly summaries
- Export reports to CSV
- Unit tests
- Web-based interface in the future

---

## 🧑‍💻 Author

Built as part of a hands-on Python learning journey by **Vishal Dsouza**  
Focused on writing **clean, readable, and extensible code**.
