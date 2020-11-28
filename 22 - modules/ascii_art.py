# program that takes in two inputs from user, a statement to print and a colour choice
# program should print the statement in the colour of choice,
# default to 'magenta' if user-selected colour is unavailable

from pyfiglet import figlet_format
from termcolor import colored

col_list = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input("What would you like to print? ")
colour = input("Which colour? ")

ascii_art = figlet_format(msg)

if colour not in col_list:
    colour = 'magenta'

colored_ascii = colored(ascii_art, color=colour)
print(colored_ascii)