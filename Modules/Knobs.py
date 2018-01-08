"""
Solves the wanted state of the knob
"""

def defuse():
    sequence = raw_input('What is the sequence?\n').strip().split(' ')
    binary_sequence = ''
    for state in sequence:
        if state == 'no':
            binary_sequence += '0'
        else:
            binary_sequence += '1'

    binary_sum = int(binary_sequence, 2)

    print {
        2:'down',
        4:'down',
        5:'up',
        6:'up',
        7:'left',
        9:'right',
        13:'right'
    }[binary_sum]
