import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spendingCategories = []

for expense in expenses.list:
    spendingCategories.append(expense.category)

spendingCounter = collections.Counter(spendingCategories)

print(spendingCategories)