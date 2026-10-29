# 🏦 Project 1: Bank Account Management System

> **A Modular Python CLI Banking Simulation**  
> *Manages customer bank accounts, balances, deposits, withdrawals, and inter-account fund transfers using in-memory dictionary state.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview

The **Bank Account Management System** is an interactive, menu-driven command-line application that simulates real-world core banking operations. It demonstrates fundamental Python data structures, state management, transaction safety guardrails, and user input validation.

---

## 🌟 Key Features

- 👤 **Account Creation**: Open a new account with an initial opening balance.
- 💵 **Deposit Funds**: Deposit money into an existing account with instant balance updates.
- 🏧 **Withdraw Money**: Securely withdraw funds with safety checks against overdrafts / insufficient balance.
- 🔁 **Account-to-Account Transfers**: Transfer money between two registered users with balance verification.
- 📊 **Balance Inquiry**: Look up the current balance of any registered account.
- 🛡️ **Error Handling**: Handles invalid numerical inputs and missing accounts gracefully.

---

## 🏗️ Code Architecture

The application uses an in-memory dictionary (`account = {}`) mapping account names to balances.

| Function | Description |
|---|---|
| `create_account()` | Checks if the user exists, prompts for initial balance, and registers the account. |
| `deposit()` | Validates account existence and credits the deposit amount to the balance. |
| `withdraw()` | Checks balance availability before debiting the requested withdrawal amount. |
| `transfer()` | Verifies both sender and receiver accounts, ensures sender has sufficient funds, and atomically transfers the amount. |
| `check_balance()` | Displays the current balance for the requested user. |
| `main()` | Provides the interactive CLI menu loop with option selection (1–6). |

---

## 🚀 How to Run

### 1. Requirements
- Python 3.8+ (No external third-party libraries required; uses Python standard library).

### 2. Execution
Run the script directly:
```bash
python bank_system.py
```
*(Or from the repository root: `python "Project 1- Bank_System.py"`)*

---

## 💻 Sample Interactive Session

```text
WELCOME TO BANK SYSTEM

1. Create
2. Deposit
3. Withdraw
4. Transfer
5. Balance
6. Exit
Enter choice (1-6): 1
Enter name: Alice
Enter amount to create account: 1000
Welcome Alice

1. Create
2. Deposit
3. Withdraw
4. Transfer
5. Balance
6. Exit
Enter choice (1-6): 1
Enter name: Bob
Enter amount to create account: 500
Welcome Bob

1. Create
2. Deposit
3. Withdraw
4. Transfer
5. Balance
6. Exit
Enter choice (1-6): 4
Sender name: Alice
Receiver name: Bob
Enter transfer amount: 300
Transfer successful

1. Create
2. Deposit
3. Withdraw
4. Transfer
5. Balance
6. Exit
Enter choice (1-6): 5
Enter name: Alice
Balance: 700

1. Create
2. Deposit
3. Withdraw
4. Transfer
5. Balance
6. Exit
Enter choice (1-6): 6
Goodbye!
```

---

## 🧠 Concepts Demonstrated

- Python Dictionaries & Nested Data Structures
- Function-based Modular Architecture
- Control Flow (`while True`, `if-elif-else`)
- Exception Handling (`try-except ValueError`)
- Defensive Programming & Transaction Logic
