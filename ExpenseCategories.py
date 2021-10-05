from budget import Expense
import timeit


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
    print(expenses.divided_for_loop)
    print(expenses.divided_set_comp)
    print(timeit.timeit(stmt="pass", setup='''from . import Expense
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')''', number=100000, globals=globals))

    if not divided_set_comp == divided_for_loop():
        print('Sets are NOT equal by == test')

    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.Issubset(b) and b.Issubset(a)):
            print("Sets are NOT equal by subset test")

if __name__ == "__main__":
    main()
