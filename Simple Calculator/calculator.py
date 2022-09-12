"""

Make a Simple Calculator which takes 2 numbers and an arithmatic operation symbol 
as input and perform the operation

"""

# input from user and storing their values in variables

num1 = int(input("Enter first Number : "))
num2 = int(input("Enter Second Number : "))
operator = input("Enter an arithmatic symbol\
    from(+, -, *, /, **, //, %) : ")

# Write if, elif, and else statements for differrent conditions

if (operator == "+"):
    print(num1, operator, num2,"=", num1+num2)
elif(operator == "-"):
    print(num1, operator, num2,"=", num1-num2)
elif(operator == "*"):
    print(num1, operator, num2,"=", num1*num2)
elif(operator == "/"):
    print(num1, operator, num2,"=", num1/num2)
elif(operator == "**"):
    print(num1, operator, num2,"=", num1**num2)
elif(operator == "//"):
    print(num1, operator, num2,"=", num1//num2)
elif(operator == "%"):
    print(num1, operator, num2,"=", num1%num2)
else:
    print("Please select correct operator !")
    
