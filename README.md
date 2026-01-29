
# 💰 Personal Finance Tracker CLI

    A command-line personal finance tracker built using **Python** that allows users to record income, expenses, and recurring subscriptions, calculate balances, and analyze spending patterns.

    This project is designed to practice **Python fundamentals**, **Object-Oriented Programming (OOP)**, and building a **realistic, extensible CLI application** similar to real-world financial tools.

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

    ---

 ## 🧠 Concepts & Skills Used

    - Python classes and objects  
    - Object-Oriented Programming (OOP)  
    - Encapsulation & separation of concerns  
    - Lists and dictionaries  
    - Loops and conditional logic  
    - User input handling & validation  
    - Data aggregation and reporting  
    - Sorting and filtering data  
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

  ### Subscription
    Represents a recurring expense.

    Stores:
    - name
    - amount
    - category
    - billing cycle (in days)
    - active status

    Subscriptions are treated as **recurring financial commitments** and are factored into adjusted balance calculations.

    ---

  ### Account
    Acts as the **core business logic layer**.

    Responsibilities:
    - Store all transactions
    - Store all subscriptions
    - Calculate:
      - Total income
      - Total expenses
      - Current balance
      - Adjusted balance (after subscriptions)
      - Expenses grouped by category
      - Monthly subscription cost
      - Top subscriptions by cost

    All calculations and aggregation live here.

    ---

  ### CLI Application
    Handles all user interaction.

    Responsibilities:
    - Display menu options
    - Collect user input
    - Create `Transaction` and `Subscription` objects
    - Delegate logic to the `Account` class
    - Display formatted output

    The CLI performs **no calculations itself**.

    ---

 ## 🔁 Data Flow

    ```
    User Input  
    ↓  
    CLI creates or queries Transactions / Subscriptions  
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

    ```bash
    python3 finance_tracker.py
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
