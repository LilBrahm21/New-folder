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
rent_percentage = (rent / income) * 100  
# calculate percent income of utilites (income/income*100) (variable)
utilities_percentage = (utilities / income) * 100  
# calculate percent income of groceries (income/income*100) (variable)
groceries_percentage = (groceries / income) * 100  
# calculate percent income of transportation (income/income*100) (variable)
transportation_percentage = (transportation / income) * 100  
# Your rent is $X.XX which is XX% of your income. (print)
spending_percentage = (spending / income) * 100  
saving_percentage = (saving / income) * 100  
# Your utilites is $XX.XX which is XX% of your income. (print)
print(f"Your rent is 1000${rent:.2f}, which is {rent_percentage:.2f}% of your income.")  
# Your groceries is $XX.XX which is XX% of your income. (print)
print(f"Your utilities is ${utilities:.2f}, which is {utilities_percentage:.2f}% of your income.")  
# Your transportation is $XX.XX which is XX% of your income. (print)
print(f"Your groceries is ${groceries:.2f}, which is {groceries_percentage:.2f}% of your income.")  
# Your savings is $XX.XX which is XX% of your income. (print)
print(f"Your transportation is ${transportation:.2f}, which is {transportation_percentage:.2f}% of your income.")  
# Your spendings is $XX.XX which is XX% of your income. (print)
print(f"Your spending is ${spending:.2f}, which is {spending_percentage:.2f}% of your income.")  
# Your savings is $XX.XX which is XX% of your income. (print)
print(f"Your saving is ${saving:.2f}, which is {saving_percentage:.2f}% of your income.")  
