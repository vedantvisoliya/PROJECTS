print("\t\tSIMPLE CALCULATOR\t\t")

# inputs 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter '1' for ADDITION\nEnter '2' for SUBTRACTION\nEnter '3' for MULTIPLICATION\nEnter '4' for DIVISION\n: "))

# functions

def add(num1,num2):
    return(num1 + num2)

def subtract(num1,num2):
    if (num1 >= num2):
        return(num1-num2)
    else:
        return(num2-num1)

def multiply(num1,num2):
    return(num1*num2)

def divide(num1,num2):
    return(num1/num2)

# logic 

if(c == 1):
    print(f"the sum of {a} + {b} = {add(a,b)}")
elif(c == 2):
    if (a > b):
        print(f"the difference of {a} - {b} = {subtract(a,b)}")  
    else:
        print(f"the difference of {b} - {a} = {subtract(a,b)}")
elif(c == 3):
    print(f"the product of {a} * {b} = {multiply(a,b)}")
elif(c == 4):
    print(f"the quotient of {a} / {b} = {divide(a,b)}")
else:
    print(ValueError)