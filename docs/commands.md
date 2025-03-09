Here are the examples of commands to run on the Command Line Interface

```bash
# Budget Management
$ python -m expense_tracker.cli set-budget --month 8 --amount 1000
# Budget set for August 2024

# Adding Expenses
$ python -m expense_tracker.cli add --category Food --amount 150 --description "Weekly groceries"
# Expense added successfully (ID: 1)

$ python -m expense_tracker.cli add --category Transport --amount 50 --description "Gas station"
# Expense added successfully (ID: 2)

$ python -m expense_tracker.cli add --category Food --amount 200 --description "Restaurant dinner"
# Expense added successfully (ID: 3)
# ⚠️  Warning: Budget exceeded by $50.00 (5% over)

# Listing Expenses
$ python -m expense_tracker.cli list
# ID  Date        Category    Description         Amount
# 1   2024-08-02  Food        Weekly groceries    $150.00
# 2   2024-08-02  Transport   Gas station         $50.00
# 3   2024-08-03  Food        Restaurant dinner   $200.00

$ python -m expense_tracker.cli list --category Food
# ID  Date        Category    Description         Amount
# 1   2024-08-02  Food        Weekly groceries    $150.00
# 3   2024-08-03  Food        Restaurant dinner   $200.00

# Updating Expenses
$  python -m expense_tracker.cli update --id 3 --amount 180
# Expense updated successfully

# Deleting Expenses
$ python -m expense_tracker.cli delete --id 2
# Expense deleted successfully

# Viewing Summaries
$ python -m expense_tracker.cli summary
# Total expenses: $480.00
# Monthly budget: $1000.00 (48% utilized)

$ python -m expense_tracker.cli summary --month 8
# August 2024 Summary:
# Total expenses: $480.00
# Budget: $1000.00 (48% utilized)
# Remaining: $520.00

$  python -m expense_tracker.cli summary --breakdown
# Category Breakdown:
# Food        $330.00 (68.8%)
# Transport   $150.00 (31.2%)

$ python -m expense_tracker.cli summary --month 8 --category Food
# August 2024 Food Expenses:
# Total: $330.00
# Budget: $500.00 (66% utilized)

# Budget Warnings
$ python -m expense_tracker.cli add --category Food --amount 300 --description "Birthday party"
# Expense added successfully (ID: 4)
# ⚠️  Warning: Budget exceeded by $130.00 (13% over)
# ⚠️  Food category exceeded by $130.00 (26% over)

$ python -m expense_tracker.cli summary --month 8
# August 2024 Summary:
# Total expenses: $780.00
# Budget: $1000.00 (78% utilized)
# Remaining: $220.00
# ⚠️  Food category: $630.00/$500.00 (26% over)
```

### This documentation shows

- Budget setting and tracking
- Expense management cycle (add/update/delete)
- Filtering and viewing options
- Real-time budget warnings
- Category-specific tracking
- Progress percentage calculations
- Multi-level warnings (total budget + category budgets)

### The system provides immediate feedback when

- Budget is exceeded
- Category limits are passed
- Budget utilization reaches warning thresholds (default >80%)
- Users approach their spending limits
