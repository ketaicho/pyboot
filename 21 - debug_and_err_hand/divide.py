# function that takes in two params and performs division
# return errors on dividing by zero or using incorrect type

def divide(num1, num2):
    try:
        result = num1/num2
    except TypeError:
        return("Please provide two integers or floats")
    except ZeroDivisionError:
        return("Please do not divide by zero")
    return result

#print(divide(5,2))
#print(divide('a',4))
print(divide(8,0))