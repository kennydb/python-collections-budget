from budget import Expense
import timeit


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    expenses.divided_for_loop = expenses.categorize_for_loop()
    expenses.divided_set_comp = expenses.categorize_set_comprehension()
    print(expenses.divided_for_loop)
    print(expenses.divided_set_comp)
    print(timeit.timeit(stmt="pass", setup='''from . import Expense
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')''', number=100000, globals=globals))


if __name__ == "__main__":
    main()
