from termcolor import colored

text = colored('hello hello', color='magenta', on_color='on_green', attrs=['blink'])
print(text)