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
    """
    Round 2 solution
    """
    sequence = raw_input('Enter the current sequence\n')
    indicator = int(sequence[0])

    if indicator == 1:
        for index, value in enumerate(sequence):
            if value == '4':
                print 'Press the button in position {}'.format(index)
                position_list.append(index)
                label_list.append('4')
                return

    if indicator == 2:
        print 'Press the button in position {}'.format(position_list[0])
        position_list.append(position_list[0])
        label_list.append(sequence[position_list[0]])
        return

    if indicator == 3:
        print 'Press the button in position 1'
        position_list.append(1)
        label_list.append(sequence[1])
        return

    if indicator == 4:
        print 'Press the button in position {}'.format(position_list[0])
        position_list.append(position_list[0])
        label_list.append(sequence[position_list[0]])
        return

def round_three():
    """
    Round 3 solution
    """
    sequence = raw_input('Enter the current sequence:\n')
    indicator = int(sequence[0])

    if indicator == 1:
        for index, value in enumerate(sequence[1:]):
            if value == label_list[1]:
                print 'Press the button in position {}'.format(index + 1)
                position_list.append(index + 1)
                label_list.append(label_list[1])
                return

    if indicator == 2:
        for index, value in enumerate(sequence[1:]):
            if value == label_list[0]:
                print 'Press the button in position {}'.format(index + 1)
                position_list.append(index + 1)
                label_list.append(label_list[0])
                return

    if indicator == 3:
        print 'Press the button in position 3'
        position_list.append(3)
        label_list.append(sequence[3])
        return

    if indicator == 3:
        for index, value in enumerate(sequence[1:]):
            if value == '4':
                print 'Press the button in position {}'.format(index + 1)
                position_list.append(index + 1)
                label_list.append('4')
                return


def round_four():
    """
    Round 4 solution
    """
    sequence = raw_input('Enter the current sequence:\n')
    indicator = int(sequence[0])
    
    if indicator == 1:
        print 'Press the button in position {}'.format(position_list[0])
        position_list.append(position_list[0])
        label_list.append(sequence[position_list[0]])
        return

    if indicator == 2:
        print 'Press the button in position 1'
        position_list.append(1)
        label_list.append(sequence[1])
        return

    if indicator == 3:
        print 'Press the button in position {}'.format(position_list[1])
        position_list.append(position_list[1])
        label_list.append(sequence[position_list[1]])
        return

    if indicator == 4:
        print 'Press the button in position {}'.format(position_list[1])
        position_list.append(position_list[1])
        label_list.append(sequence[position_list[1]])
        return

def round_five():
    pass
