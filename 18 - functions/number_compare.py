# function to compare two numbers and return greater number

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

def number_compare(num1=0, num2=0):
    if (num1 > num2):
        return "First is greater"
    elif (num2 > num1):
        return "Second is greater"
    elif (num1 == num2):
        return "Numbers are equal"
    else:
        "Please enter valid selection"

print(number_compare(num1, num2))