#Brahm Brar Fiancial Calculator Update Python
def info(cost, income, type):
    percentage = cost/income*100
    print(f"Your {type} is ${cost:.2f}, which is {percentage} percent of your income.")

name = input("What is your name?\n")


def user(answer):
    pregunta = (f"What is your {answer} ?\n")
    return float(input(pregunta))

income = user("income")
rent = user("rent")
utilities = user("utilities")
groceries = user("groceries")
transportation = user("transportation")
savings = income*.1
spending = income-savings-rent-utilities-groceries-transportation

info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")