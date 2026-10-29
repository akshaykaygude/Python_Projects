# 🐍 Modular Python CLI Applications Collection

> **A curated showcase of 4 modular, interactive Python command-line projects.**  
> *Demonstrating core data structures, object-oriented programming (OOP), algorithm design, time parsing, and system architecture with zero external dependencies.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Projects](https://img.shields.io/badge/Projects-4%20Interactive%20Apps-brightgreen.svg)](#-project-showcase)
[![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-blue.svg)](#-zero-setup-quickstart)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Project Showcase

| # | Project | Description | Core Concepts | Documentation |
|:---:|---|---|---|:---:|
| **01** | [**Bank System**](01-Bank-System/) | Simulated core banking CLI with account creation, deposits, withdrawals, and account-to-account fund transfers. | Dictionaries, Transaction Guardrails, State Tracking | [Read Guide ➡️](01-Bank-System/README.md) |
| **02** | [**Task Scheduler**](02-Task-Scheduler/) | Priority task manager that sorts deadlines chronologically and manages the completion lifecycle. | `datetime` Parsing, Lambda Sorting, Data Filtering | [Read Guide ➡️](02-Task-Scheduler/README.md) |
| **03** | [**Mini Social Network**](03-Mini-Social-Network/) | OOP social media platform with user authentication, posting, follow/unfollow social graphs, and dynamic feeds. | OOP (Classes), Authentication, Sets, Feed Aggregation | [Read Guide ➡️](03-Mini-Social-Network/README.md) |
| **04** | [**Short URL Maker**](04-Short-URL-Maker/) | In-memory URL shortener using Base62 encoding, collision resolution, and bidirectional $O(1)$ lookups. | System Design, Base62 Combinatorics, Hash Tables | [Read Guide ➡️](04-Short-URL-Maker/README.md) |

---

## 📁 Repository Structure

```text
Python_Projects/
├── 01-Bank-System/
│   ├── bank_system.py                 # Clean modular banking implementation
│   └── README.md                      # Detailed project documentation & walkthrough
├── 02-Task-Scheduler/
│   ├── task_scheduler.py              # Chronological task manager
│   └── README.md                      # Detailed project documentation & walkthrough
├── 03-Mini-Social-Network/
│   ├── mini_social_network.py         # Object-oriented social media simulation
│   └── README.md                      # Detailed project documentation & walkthrough
├── 04-Short-URL-Maker/
│   ├── short_url_maker.py             # Base62 URL shortener
│   └── README.md                      # Detailed project documentation & walkthrough
├── Project 1- Bank_System.py          # Root entrypoint
├── Project 2- Task Scheduler.py       # Root entrypoint
├── Project 3- Mini_Social_Network.py  # Root entrypoint
├── Project 4- Short URL Maker.py      # Root entrypoint
├── LICENSE                            # MIT License
└── README.md                          # Master portfolio overview
```

---

## ⚡ Zero-Setup Quickstart

All projects in this repository are built exclusively with the **Python Standard Library**. No `pip install` or external packages are required!

### 1. Clone the Repository
```bash
git clone https://github.com/akshaykaygude/Python_Projects.git
cd Python_Projects
```

### 2. Run Any Project

```bash
# Project 1: Bank System
python 01-Bank-System/bank_system.py

# Project 2: Priority Task Scheduler
python 02-Task-Scheduler/task_scheduler.py

# Project 3: Mini Social Network
python 03-Mini-Social-Network/mini_social_network.py

# Project 4: Short URL Maker
python 04-Short-URL-Maker/short_url_maker.py
```

*(You can also run any script directly from the root using its original filename, e.g. `python "Project 1- Bank_System.py"`)*

---

## 🧠 Skills & Engineering Concepts Matrix

| Project | Dictionaries & Hash Tables | OOP & Classes | Date/Time Processing | Validation & Guardrails | System Design Principles |
|---|:---:|:---:|:---:|:---:|:---:|
| **01. Bank System** | ✅ | — | — | ✅ (Overdraft Prevention) | Transaction Atomicity |
| **02. Task Scheduler** | ✅ | — | ✅ (`strptime` / `strftime`) | ✅ (Date Formatting) | Priority Queuing |
| **03. Mini Social Network** | ✅ | ✅ | ✅ (Post Timestamps) | ✅ (Auth & Duplicates) | Social Graph & Feed Aggregation |
| **04. Short URL Maker** | ✅ | ✅ | — | ✅ (Collision Checks) | Bidirectional Caching & Base62 |

---

## 📄 License

This repository is open-source and available under the [MIT License](LICENSE).
