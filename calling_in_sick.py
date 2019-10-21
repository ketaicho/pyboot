# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# set this to True or False with Boolean Logic and Conditionals!
calling_in_sick = None

if actually_sick and (sick_days > 0 or sick_days <= 10):
    calling_in_sick = True
elif kinda_sick and hate_your_job and (sick_days > 0 or sick_days <= 10):
    calling_in_sick = True
else:
    calling_in_sick = False

print(f"Are you calling in sicK? {calling_in_sick}")