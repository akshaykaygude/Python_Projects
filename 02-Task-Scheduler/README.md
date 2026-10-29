# ⏰ Project 2: Priority Task Scheduler

> **A Chronological CLI Task & Reminder Organizer**  
> *Schedules tasks with due dates, sorts them in priority order, tracks completion status, and maintains history using Python's `datetime` module.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview

The **Priority Task Scheduler** is a command-line productivity tool that helps users organize their deadlines. Unlike basic to-do lists, it parses full date-time strings, automatically sorts pending tasks by their chronological urgency (earliest due date first), and tracks task completion lifecycle.

---

## 🌟 Key Features

- 📅 **Date & Time Parsing**: Supports standard `YYYY-MM-DD HH:MM` timestamp format validated through `datetime.strptime`.
- ⚡ **Auto-Sorting by Due Date**: Pending tasks are automatically sorted chronologically using lambda sorting.
- ✅ **Task Completion Lifecycle**: Mark tasks completed by their index number, moving them from pending to completed.
- 📋 **Separated Views**: Dedicated views for **Pending Tasks** and **Completed Tasks**.
- 🛡️ **Defensive Error Handling**: Rejects malformed dates and invalid selection indices without crashing.

---

## 🏗️ Code Architecture

The application stores tasks in a list of dictionary items (`tasks = []`), where each task has:
- `name` *(str)*: Title or description of the task
- `due` *(datetime)*: Parsed datetime object representing the deadline
- `done` *(bool)*: Boolean flag tracking completion status

| Function | Description |
|---|---|
| `add_task()` | Prompts for name and due date, validates date format, and appends the new task. |
| `show_pending(show_index)` | Sorts pending tasks by `due` timestamp and renders them with optional numeric indices. |
| `complete_task()` | Prompts the user to pick a pending task by index number and flips `task['done'] = True`. |
| `show_completed()` | Filters and prints all tasks marked as completed. |

---

## 🚀 How to Run

### 1. Requirements
- Python 3.8+ (No external third-party libraries required; uses Python built-in `datetime`).

### 2. Execution
Run the script directly:
```bash
python task_scheduler.py
```
*(Or from the repository root: `python "Project 2- Task Scheduler.py"`)*

---

## 💻 Sample Interactive Session

```text
1.Add  2.Complete  3.Pending  4.Completed  5.Exit
Choose: 1
Task name: Prepare Quarterly Sales Report
Due date (YYYY-MM-DD HH:MM): 2026-11-01 10:00
Task added.

1.Add  2.Complete  3.Pending  4.Completed  5.Exit
Choose: 1
Task name: Team Standup Meeting
Due date (YYYY-MM-DD HH:MM): 2026-10-30 09:30
Task added.

1.Add  2.Complete  3.Pending  4.Completed  5.Exit
Choose: 3

Pending Tasks:
- Team Standup Meeting
- Prepare Quarterly Sales Report

1.Add  2.Complete  3.Pending  4.Completed  5.Exit
Choose: 2

Pending Tasks:
1. Team Standup Meeting - 2026-10-30 09:30
2. Prepare Quarterly Sales Report - 2026-11-01 10:00
Enter task number to complete: 1
Marked complete.

1.Add  2.Complete  3.Pending  4.Completed  5.Exit
Choose: 4

Completed Tasks:
- Team Standup Meeting

1.Add  2.Complete  3.Pending  4.Completed  5.Exit
Choose: 5
```

---

## 🧠 Concepts Demonstrated

- Python `datetime` module (`datetime.strptime`, `datetime.strftime`)
- Lambda expressions & sorting keys (`sorted(tasks, key=lambda t: t['due'])`)
- State management with lists of dictionaries
- Data filtering & index mapping
- Exception handling for robust CLI user interaction
