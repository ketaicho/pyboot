# function takes 4 parameters (a list, command, location, value)

def list_manipulation(lst, cmd, loc, val):
    if (cmd == 'remove') & (loc == 'end'):
        return lst.pop(-1)
    elif (cmd =='remove') & (loc == 'beginning'):
        return lst.pop(0)
    elif (cmd == 'add') & (loc == 'beginning'):
        lst.insert(0, val)
        return lst
    elif (cmd == 'add') & (loc == 'end'):
        lst.append(val)
        return lst

lst = [1,2,3,4]

#cmd = 'remove'
cmd = 'add'

#loc = 'beginning'
loc = 'end'

print(list_manipulation(lst, cmd, loc, val=8))
