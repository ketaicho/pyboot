# function to return the day of the week, based on the parameter (number) passed in

from random import randint

randVal = randint(1, 7)

print(f"Value of random number: {randVal}")

day_of_week = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

def return_day(randVal=1):
    return day_of_week.get(randVal)

print(return_day(randVal))
