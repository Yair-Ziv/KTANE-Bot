"""
Solve for the memory modules
"""
round_num = 1
position_list = []
label_list = []

def defuse():
    global round_num
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
    
    round_num += 1

def round_one():
    """
    Solve for round one
    """
    sequence = raw_input('Enter the current sequence:\n')
    indicator = int(sequence[0])
    if indicator == 1:
        print 'Press the button in position 2'
        position_list.append(2)
        label_list.append(sequence[2])
        return

    if indicator == 2:
        print 'Press the button in position 2'
        position_list.append(2)
        label_list.append(sequence[2])
        return

    if indicator == 3:
        print 'Press the button in position 3'
        position_list.append(3)
        label_list.append(sequence[3])
        return

    if indicator == 4:
        print 'Press the button in position 4'
        position_list.append(4)
        label_list.append(sequence[4])
        return

def round_two():
    sequence = raw_input('Enter the current sequence\n')
    indicator = int(sequence[0])

    if indicator == 1:
        for index, value in enumerate(sequence):
            if value == '4':
                print 'Press the button in position {}'.format(index)
                return

    if indicator == 2:
        print 'Press the button in position {}'.format(position_list[0])
        return

    if indicator == 3:
        print 'Press the button in position 1'
        return

    if indicator == 4:
        print 'Press the button in position {}'.format(position_list[0])
        position_list.append(4)
        label_list.append(sequence[4])
        return

def round_three():
    pass

def round_four():
    pass

def round_five():
    pass
