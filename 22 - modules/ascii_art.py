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