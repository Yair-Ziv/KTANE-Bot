"""
Solver for the simple wires modules.
"""

_last_digit = None

def defuse(last_digit):
    """
    Main complicated wires defusal function, that get's 
    split into 3 sub-functions that solve depending
    on the number of wires in the module.
    """
    _last_digit = last_digit
    wires = raw_input('Enter the wire sequence:\n').split(', ')
    if(len(wires) == 3):
        case_3(wires)
        return
    elif(len(wires) == 4):
        case_4(wires)
        return
    elif(len(wires) == 5):
        case_5(wires)
        return
    else:
        case_6(wires)
        return

def case_3(wires):
    red_count = 0
    blue_count = 0
    for wire in wires:
        if wire == 'red':
            red_count += 1
        elif wire == 'blue':
            blue_count += 1
    
    #If there are no red wires, cut the second wire
    if red_count == 0:
        print 'Cut the 2nd wire'
        return
    
    #Otherwise, if the last wire is white, cut the last wire
    if wires[-1] == 'white':
        print 'Cut the last wire'
        return

    if blue_count > 1:
        if wires[2] == 'blue':
            print 'Cut the 3rd wire'
            return
        else:
            print 'Cut the 2nd wire'
            return
    
    print 'Cut the last wire'
    return

def case_4(wires):
    pass

def case_5(wires):
    pass

def case_6(wires):
    pass