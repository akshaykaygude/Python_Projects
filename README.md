# 🐍 Modular Python CLI Applications Collection

> **A curated showcase of 4 modular, interactive Python command-line projects.**  
> *Demonstrating core data structures, object-oriented programming (OOP), algorithm design, time parsing, and system architecture using exclusively the Python Standard Library.*

[![CLI Projects CI](https://github.com/akshaykaygude/Python_Projects/actions/workflows/ci.yml/badge.svg)](https://github.com/akshaykaygude/Python_Projects/actions/workflows/ci.yml)
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

## 🎯 Current Capabilities: What Already Works

- [x] **01. Bank Account Management System**:
  - Validates opening balance inputs and registers unique account owners.
  - Guards against overdrafts and maintains balance integrity during transfers.
- [x] **02. Priority Task Scheduler**:
  - Parses standard timestamps (`YYYY-MM-DD HH:MM`) using `datetime.strptime`.
  - Auto-sorts pending deadlines in ascending chronological priority order.
  - Supports task completion state toggling and dedicated pending/completed views.
- [x] **03. Mini Social Network**:
  - Encapsulated OOP class design managing authentication, session state, and user dictionaries.
  - Multi-user follow graphs using Python `set()` to eliminate duplicate relationships.
  - Reverse-chronological newsfeed aggregating posts from the author and followed users.
- [x] **04. Short URL Maker**:
  - Generates compact 6-character Base62 keys ($62^6 pprox 56.8\text{ billion}$ permutations).
  - Bidirectional hash map with collision detection loop and idempotent caching.
- [x] **Automated Test Suite & Multi-Version CI (`tests/test_cli_projects.py`, `.github/workflows/ci.yml`)**:
  - Unit tests covering all 4 projects running across Python 3.8, 3.9, 3.10, and 3.11 on GitHub Actions.

---

## ⚠️ Known Limitations & Real-World Edge Cases

1. **In-Memory State Volatility**:
   - All 4 projects utilize in-memory Python data structures (dictionaries and lists). Session data resets upon process termination.
2. **Plaintext Passwords in Social Network Demo**:
   - The educational implementation stores passwords in-memory without hashing. In a production deployment, industry-standard cryptographic hashing (`bcrypt`/`argon2`) would be enforced.
3. **Local Timezone Assumption in Scheduler**:
   - Dates are parsed without timezone offsets (`tzinfo`), assuming the local system clock for all deadline comparisons.

---

## 🗺️ Engineering Roadmap & Future Milestones

- [x] **v1.0 (Core Logic)**: 4 working CLI applications with clean modular structure.
- [x] **v1.1 (Testing & CI)**: Comprehensive unit test suite and multi-version GitHub Actions CI pipeline.
- [ ] **v2.0 (Persistent Storage)**: Add SQLite / JSON file persistence so state survives program restarts.
- [ ] **v2.1 (Security Hardening)**: Integrate `hashlib`/`bcrypt` for password hashing and salting.
- [ ] **v2.2 (Web API / GUI)**: Build lightweight FastAPI REST endpoints for the Short URL maker and Bank system.

---

## 📁 Repository Structure

```text
Python_Projects/
├── .github/workflows/
│   └── ci.yml                         # Automated GitHub Actions test pipeline
├── tests/
│   └── test_cli_projects.py           # Unit tests covering all 4 applications
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
├── LICENSE                            # MIT Open-Source License
└── README.md                          # Master portfolio overview
```

---

## ⚡ Zero-Setup Quickstart

All applications run exclusively on the **Python Standard Library**. No external dependencies or `pip install` required!

### 1. Clone the Repository
```bash
git clone https://github.com/akshaykaygude/Python_Projects.git
cd Python_Projects
```

### 2. Run Any Application
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

### 3. Run Automated Tests
```bash
python -m unittest tests/test_cli_projects.py
```

---

## 📄 License

This repository is open-source and available under the [MIT License](LICENSE).
