# Expense Tracker Documentation 📊

![CLI Expense Tracker](https://img.shields.io/badge/CLI-Expense_Tracker-blueviolet)

A command-line application for managing personal finances with category support and monthly tracking.

## Table of Contents

- [Installation](#installation-)
- [Basic Usage](#basic-usage-)
- [Features](#features-)
- [Command Reference](#command-reference-)
  - [Add Expense](#add-expense)
  - [List Expenses](#list-expenses)
  - [Delete Expense](#delete-expense)
  - [Update Expense](#update-expense)
  - [View Summary](#view-summary)
- [Examples](#examples-)
- [Data Management](#data-management-)
- [Troubleshooting](#troubleshooting-)

## Installation 💻

### Requirements

- Python 3.8+
- pip package manager

### Steps

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
pip install -e .
```

## Basic Usage 🛠️

expense-tracker [command] [options]

### Features 🌟

- ✅ Add expenses with categories
- 🔄 Update existing entries
- ❌ Delete expenses
- 📅 Monthly filtering
- 🗂️ Category-based filtering
- 📊 Financial summaries
- 💾 Automatic JSON storage

#### Command Reference 📖

Add Expense

```sh
expense-tracker add --description "Text" --amount X.X --category "Category"

Required Flags:
--description: Expense description (string)
--amount: Positive number (>0)
--category: Expense category
```

List Expenses

```bash
expense-tracker list [--category CATEGORY] [--month MONTH]
Options:
--category: Filter by category (case-insensitive)
--month: Filter by month (1-12)

Output:
ID  Date        Category    Description         Amount
1   2024-08-01  Food        Groceries           $50.00
2   2024-08-02  Transport   Gas                 $40.00
```

Delete Expense

```bash
expense-tracker delete --id ID
```

Update Expense

```bash
expense-tracker update --id ID [--description TEXT] [--amount X.X] [--category CATEGORY]
Options:
At least one of: description, amount, or category
```

View Summary

```bash
expense-tracker summary [--month M] [--category C] [--breakdown]
Options:
--month: Show specific month's total
--category: Filter by category
--breakdown: Show category distribution

Example Output:

Total expenses: $90.00
---
Category Breakdown:
Food        $50.00 (55.6%)
Transport   $40.00 (44.4%)
```

### Examples 🧑💻

Add weekly expenses:

```bash
expense-tracker add --description "Coffee" --amount 4.5 --category Food
expense-tracker add --description "Taxi" --amount 15 --category Transport
```

Generate monthly report:

```bash
expense-tracker summary --month 8 --breakdown
```

Manage entries:

```bash
expense-tracker list --category food
expense-tracker update --id 2 --amount 18
expense-tracker delete --id 5
```

### Data Management 💾

All data stored in expenses.json

- ⚠️ Never edit manually while application is running
- 🔄 Automatic backup on every change

### Troubleshooting 🚨

#### Error Solution

- "Amount must be positive" Use values > 0
- "Category cannot be empty" Provide valid --category flag
- "Invalid month" Use 1-12 (Jan-Dec)
- "Expense ID not found" Verify ID with expense-tracker list

Happy Financial Tracking! 🎉
