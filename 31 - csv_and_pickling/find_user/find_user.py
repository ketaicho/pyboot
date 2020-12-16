# function that takes in a first and last name
# uses that to find if the username is in the csv file

from csv import reader

def find_user(fname, lname):
    with open('users.csv', newline='') as csvfile:
        fileReader = reader(csvfile, delimiter=',')
        next(fileReader)

        nameList = list(fileReader)
        print(nameList)

        name = fname + " " + lname
        print(f'name: {name}')

        for count, row in enumerate(fileReader, start=1):
           joinName = " ".join(row)
           print(f'joinName: {joinName}')
           if (joinName == name):
               return count
           return "User not found!"

fname = input("Enter first name: ")
lname = input("Enter last name: ")

print(find_user(fname, lname))