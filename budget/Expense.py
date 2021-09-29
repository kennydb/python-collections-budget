import csv
from datetime import datetime


class Expense():
    def __init__(self, date_str, vendor, category, amount):
        self.date_time = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        self.vendor = vendor
        self.category = category
        self.amount = amount


class Expenses():
    def __init__(self):
        self.list = []
        self.sum = 0

    # Read in the December spending data, row[2] is the $$, and need to format $$
    def read_expenses(self, filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if '-' not in row[3]:
                    continue
                amount = float((row[3][2:]).replace(',', ''))
                self.list.append(Expense(row[0], row[1], row[2], amount))
                self.sum += amount

    def categorize_for_loop(self):
        necessary_expenses = set()
        food_expenses = set()
        unnecessary_expenses = set()
        for i in self.list:
            if (i.category == 'Phone' or i.category == 'Auto and Gas' or
                    i.category == 'Classes' or i.category == 'Utilities' or
                    i.category == 'Mortgage'):
                necessary_expenses.add(i)
            elif (i.category == 'Groceries' or i.category == 'Eating Out'):
                food_expenses.add(i)
            else:
                unnecessary_expenses.add(i)
                divided_for_loop = self.categorize_for_loop

        return [necessary_expenses, food_expenses, unnecessary_expenses]

    def categorize_set_comprehension(self):
        pass
        # necessary_expenses = {x for x in self.list}
        # if (self.x.category == 'Phone' or self.x.category == 'Auto and Gas' or
        #         self.x.category == 'Classes' or self.x.category == 'Utilities' or
        #         self.x.category == 'Mortgage') in self.list:
        #             necessary_expenses.add(self.x.category)
        #             food_expenses = {x for x in self.list}
        # if self.x.category == 'Groceries' or self.x.category == 'Eating Out':
        #         unnecessary_expenses = set(list) - (necessary_expenses + food_expenses)

        # return [necessary_expenses, food_expenses, unnecessary_expenses]

    # divided_set_comp = categorize_set_comprehension()

    # if not divided_set_comp == divided_for_loop:
    #     print('Sets are NOT equal by == test')
    #     for a,b in zip(divided_for_loop, divided_set_comp):
    #         if not set.issubset(a, b):
    #             print("Sets are NOT equal by subset test")
