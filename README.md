# expense-tracker-cli

![CLI Expense Tracker](https://img.shields.io/badge/CLI-Expense_Tracker-blueviolet)

# Add with category
$ expense-tracker add --category "Food" --description "Lunch" --amount 20

# List by category
$ expense-tracker list --category food

# Category breakdown
$ expense-tracker summary --breakdown
# Category          Amount
# Food              $50
# Transportation    $30

# Monthly category summary
$ expense-tracker summary --month 8 --category food
# Total food expenses for August: $150