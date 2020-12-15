# function that reads from a csv file and prints content
import csv

def print_user():
    with open('users.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        #next(filereader)
        for row in filereader:
            print(' '.join(row))

print_user()