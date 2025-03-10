# Expense Tracker CLI 💸

A Python-based command-line application for managing personal finances with budget tracking and CSV exports.

## Project_URL

https://roadmap.sh/projects/expense-tracker

## 🚀 Quick Start

### Prerequisites

Python 3.8+
pip package manager

### Installation

- **Clone the repository:**

```bash
git clone <https://github.com/yourusername/expense-tracker.git>
cd expense-tracker
```

- **Create virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

- **Install dependencies:**

```bash
pip install -e .
```

### 📖 Basic Usage

- **Run Commands**

```bash
python -m expense_tracker.cli [COMMAND] [OPTIONS]
```

or

```bash
expense-tracker [COMMAND] [OPTIONS]
```

#### Common Commands

##### Command Options Example

```bash
- add --category, --amount, --desc 
    # python -m expense_tracker.cli add --category Food --amount 15 --desc "Lunch"

- list --month, --category 
    # python -m expense_tracker.cli list --month 8

- set-budget --month, --amount 
    # python -m expense_tracker.cli set-budget --month 8 --amount 1000

- export --output, --month, --category 
    # python -m expense_tracker.cli export --output expenses.csv
```

##### 💡 Example Workflow

- **Set a monthly budget:**

```bash
python -m expense_tracker.cli set-budget --month 8 --amount 500
```

- **Add expenses:**

```bash
python -m expense_tracker.cli add --category Food --amount 50 --desc "Groceries"
```

- **Check budget status:**

```bash
python -m expense_tracker.cli summary --month 8
```

- **Export data:**

```bash
python -m expense_tracker.cli export --output expenses.csv
```

### 📁 Data Management

**Data stored in project root:**

- expenses.json: Expense records

- budgets.json: Budget settings

Exported CSV files where specified

## 🚨 Troubleshooting

### Permission Errors

```bash
# Linux/Mac
chmod +x venv/bin/activate

# Windows: Run as Administrator
```

### Missing Dependencies

```bash
pip install -r requirements.txt
```

### Update Application

```bash
git pull origin main
pip install --upgrade -e .
```

## 📄 License

MIT License - See LICENSE for details

**To uninstall:**

```bash
pip uninstall expense-tracker
rm -rf venv/
```
