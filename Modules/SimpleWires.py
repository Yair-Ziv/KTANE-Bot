"""
Solver for the simple wires modules.
"""

def defuse(last_digit):
    """
    Main complicated wires defusal function, that get's 
    split into 3 sub-functions that solve depending
    on the number of wires in the module.
    """
    wires = raw_input('Enter the wire sequence:\n').split(', ')
    if(len(wires) == 3):
        case_3(wires)
        return
    elif(len(wires) == 4):
        case_4(wires, last_digit)
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

def case_4(wires, last_digit):
    """
    Solve for the case of 4 wires
    """
    red_count = 0
    blue_count = 0
    yellow_count = 0
    #Counting the number of appearances of each wire color.
    for wire in wires:
        if wire == 'red':
            red_count += 1
        elif wire == 'blue':
            blue_count += 1
        elif wire == 'yellow':
            yellow_count += 1
    
    #If there is more than one red wire and the last digit
    #of the serial number is odd, but the last red wire
    if red_count > 1 and last_digit % 2 == 1:
        for i in range(len(wires) - 1, 0, -1):
            if wires[i] == 'red':
                print 'Cut the wire in position {}'.format(i  + 1)
                return
    
    #Otherwise, if the last wire is yellow and there are no red wires
    #Cut the first wire
    if wires[-1] == 'yellow' and red_count == 0:
        print 'Cut the first wire'
        return

    #Otherwise, if there is exactly one blue wire, cut the first wire
    if blue_count == 1:
        print 'Cut the first wire'
        return

    if yellow_count > 1:
        print 'Cut the last wire'
        return

    print 'Cut the second wire'
    return


def case_5(wires):
    pass

def case_6(wires):
    pass