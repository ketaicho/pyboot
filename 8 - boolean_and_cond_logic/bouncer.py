print("Enter your age: ")
age = input()
if age:
    age = int(float(age))
    if age >= 21:
        print("You are good to enter and can drink!")
    elif age >= 18:
        print("You can enter, but you need a wristband!")
    else:
        print("You can't come in, little one!")
else:
    print("Please enter a valid age!")