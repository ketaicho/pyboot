# function to compare two numbers and return greater number

num1 = input("Enter first number: ")
num2 = input("Enter seconmd number: ")

# this approach used to demonstrate 'ternary conditional'
# also, this solution negates the different conditions to cater for
def number_compare(num1=0, num2=0):
    return "First is greater" if (num1 > num2) else "Second is greater"

print(number_compare(num1, num2))