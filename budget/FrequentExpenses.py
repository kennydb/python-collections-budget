import budget.Expense
from budget import *
import collections
import matplotlib.pyplot as plt


filepath = 'data/spending_data.csv'
expenses = budget.Expense.Expenses()
expenses.read_expenses(filepath)

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)


top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()

print(spending_counter)
print(top5)
print(categories, count)
