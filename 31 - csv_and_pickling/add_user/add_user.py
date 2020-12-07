# function that takes in a first name and last name, adds a new user to csv file
from csv import DictWriter

def add_user(firstn, lastn):
    with open('users.csv', 'a', newline='') as csvfile:
        fields = ['First Name', 'Last Name']
        writer = DictWriter(csvfile, fieldnames=fields)

        #writer.writeheader()
        writer.writerow({'First Name': firstn, 'Last Name': lastn})


fname = input("Enter first name: ")
lname = input("Enter last name: ")

add_user(fname,lname)

print('Done!')
