"""
Solve for the memory modules
"""
round_num = 1
position_list = []
label_list = []

def defuse():
    if round_num == 1:
        round_one()
    if round_num == 2:
        round_two()
    if round_num == 3:
        round_three()
    if round_num == 4:
        round_four()
    if round_num == 5:
        round_five()

def round_one():
    """
    Solve for round one
    """
    sequence = raw_input('Enter the current sequence: ')
    indicator = int(sequence[0])
    if indicator == 1:
        print 'Press the button in the second position'
        position_list.append(2)
        label_list.append(sequence[2])
        return

    if indicator == 2:
        print 'Press the button in the second position'
        position_list.append(2)
        label_list.append(sequence[2])
        return

    if indicator == 3:
        print 'Press the button in the third position'
        position_list.append(3)
        label_list.append(sequence[3])
        return

    if indicator == 4:
        print 'Press the button in the fourth position'
        position_list.append(4)
        label_list.append(sequence[4])
        return

def round_two():
    pass

def round_three():
    pass

def round_four():
    pass

def round_five():
    pass
