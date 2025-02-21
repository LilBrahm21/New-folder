#Brahm Brar Fiancial Calculator Python

# print statement that welcomes user and tells what program does

# ask what their income is(varible an input)
income= float (input("what is your inocme?\n"))
# ask what their rent is(varible an input)
rent= float(input("what is your rent?\n"))
# ask what their utilites is(varible an input)
utilities= float (input("what is your utilites?\n"))
# ask what their groceries is(varible an input)
groceries= float (input("what is your groceries?\n"))
# ask what their transportation is(varible an input)
transportation= float (input("what is your transportation?\n"))
# calculate savings as 10% of income (income*.1) (variable)
saving= income*.1
# calculate spending as income-savings-rent-utilites-groceries-transportation (variable)
spending = income-rent-utilities-groceries-transportation
# calculate percent income of rent (income/income*100) (variable)
rent_percentage = rent//income *100
# calculate percent income of utilites (income/income*100) (variable)
utilities_percentage = utilities//income *100
# calculate percent income of groceries (income/income*100) (variable)
groceries_percentage = groceries//income *100
# calculate percent income of transportation (income/income*100) (variable)
transportation_percentage = transportation//income *100
# Your rent is $X.XX which is XX% of your income. (print)
spending_percentage = spending//income *100
saving_percentage = saving//income *100
# Your utilites is $XX.XX which is XX% of your income. (print)
print("your rent is $", rent, "which is" ,rent_percentage, "of your income")
# Your groceries is $XX.XX which is XX% of your income. (print)
print("your utilities is $", utilities, " ,which is" , utilities_percentage, "of your income")
# Your transportation is $XX.XX which is XX% of your income. (print)
print("your groceries is $", groceries, "which is" , groceries_percentage, "of your income")
# Your savings is $XX.XX which is XX% of your income. (print)
print("your transportation is $", transportation, "which is" , transportation_percentage, "of your income") 
# Your spendings is $XX.XX which is XX% of your income. (print)
print("your spending is $", spending, "which is" , spending_percentage, "of your income")
# Your savings is $XX.XX which is XX% of your income. (print)
print("your saving is $", saving, "which is" , saving_percentage, "of your income")