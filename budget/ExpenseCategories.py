from . import Expense
import timeit


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = categorize_set_comprehension()

    print(timeit.timeit(stmt="pass", setup='''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')''', number=100000, globals=globals))


if __name__ == "__main__":
    main()
