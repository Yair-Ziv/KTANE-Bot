"""
Solve for the wire sequence module
Requires: Nothing
"""

blue_count = 0
red_count = 0
black_count = 0

CUT_MESSAGE = 'cut'
NOT_CUT_MESSAGE = 'don\'t cut'

def defuse():
    """
    Main defusal function that splits to each individual color
    """
    wire_sequence = raw_input('What is the sequence?\n').strip().split(' ')

    output = ''
    for index in range(0, len(wire_sequence), 2):
        if wire_sequence[index] == 'red':
            output += defuse_red(str(wire_sequence[index + 1])[0])
        elif wire_sequence[index] == 'blue':
            output += defuse_blue(str(wire_sequence[index + 1])[0])
        elif wire_sequence[index] == 'black':
            output += defuse_black(str(wire_sequence[index + 1])[0])

        output += ', '

    print output

def defuse_red(connected_to):
    """
    Checks wether to cut the current black wire
    """
    global red_count
    red_count += 1
    return {
        1:CUT_MESSAGE if connected_to == 'c' else NOT_CUT_MESSAGE,
        2:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
        3:CUT_MESSAGE if connected_to == 'a' else NOT_CUT_MESSAGE,
        4:CUT_MESSAGE if connected_to == 'a' or connected_to == 'c' else NOT_CUT_MESSAGE,
        5:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
        6:CUT_MESSAGE if connected_to == 'a' or connected_to == 'c' else NOT_CUT_MESSAGE,
        7:CUT_MESSAGE,
        8:CUT_MESSAGE if connected_to == 'a' or connected_to == 'b' else NOT_CUT_MESSAGE,
        9:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
    }[red_count]


def defuse_blue(connected_to):
    """
    Checks wether to cut the current black wire
    """
    global blue_count
    blue_count += 1
    return {
        1:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
        2:CUT_MESSAGE if connected_to == 'a' or connected_to == 'c' else NOT_CUT_MESSAGE,
        3:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
        4:CUT_MESSAGE if connected_to == 'a' else NOT_CUT_MESSAGE,
        5:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
        6:CUT_MESSAGE if connected_to == 'b' or connected_to == 'b' else NOT_CUT_MESSAGE,
        7:CUT_MESSAGE if connected_to == 'c' else NOT_CUT_MESSAGE,
        8:CUT_MESSAGE if connected_to == 'a' or connected_to == 'c' else NOT_CUT_MESSAGE,
        9:CUT_MESSAGE if connected_to == 'a' else NOT_CUT_MESSAGE,
    }[blue_count]

def defuse_black(connected_to):
    """
    Checks wether to cut the current black wire
    """
    global black_count
    black_count += 1

    return {
        1:CUT_MESSAGE,
        2:CUT_MESSAGE if connected_to == 'a' or connected_to == 'c' else NOT_CUT_MESSAGE,
        3:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
        4:CUT_MESSAGE if connected_to == 'a' or connected_to == 'c' else NOT_CUT_MESSAGE,
        5:CUT_MESSAGE if connected_to == 'b' else NOT_CUT_MESSAGE,
        6:CUT_MESSAGE if connected_to == 'b' or connected_to == 'c' else NOT_CUT_MESSAGE,
        7:CUT_MESSAGE if connected_to == 'a' or connected_to == 'b' else NOT_CUT_MESSAGE,
        8:CUT_MESSAGE if connected_to == 'c' else NOT_CUT_MESSAGE,
        9:CUT_MESSAGE if connected_to == 'c' else NOT_CUT_MESSAGE
    }[black_count]
