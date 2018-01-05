"""
Complicated Wires solver
Requires: Last digit of the serial, has a parallel port, battert count
TODO Find text model that fits
TODO Enhance the program by converting the values (red, blue, light, star)
to binary values, then calculate to decimal and check by sum
"""

CUT_MESSAGE = 'cut'
NOT_CUT_MESSAGE = 'do not cut'

def defuse(last_digit, has_parallel, battery_count):
    """
    Solves the complicated wires module
    """
    wire_sequence_raw = raw_input('Enter the wire sequence:\n').strip().split('next')
    wire_sequence = []
    for wire in wire_sequence_raw:
        wire = str(wire).strip()
        wire_sequence.append(str(wire).split(' '))

    output_sequence = ''
    for wire in wire_sequence:
        output_sequence += _defuse_wire(wire, last_digit % 2 == 0, has_parallel, battery_count)
        output_sequence += ', '
    
    print output_sequence


def _defuse_wire(wire, last_digit_even, has_parallel, battery_count):
    """
    Defuses each wire independently
    """
    is_red = False
    is_blue = False
    is_star = False
    is_light = False

    #If there is nothing on the wire.
    if len(wire) == 0:
        return 'cut'

    for identifier in wire:
        if identifier == 'red':
            is_red = True
        elif identifier == 'blue':
            is_blue = True
        elif identifier == 'star':
            is_star = True
        elif identifier == 'light' or identifier == 'led':
            is_light = True

    if is_red and is_blue and is_star and is_light:
        return NOT_CUT_MESSAGE

    if is_red and is_blue and is_star:
        return CUT_MESSAGE if has_parallel else NOT_CUT_MESSAGE

    if is_red and is_blue and is_light:
        return CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE

    if is_red and is_star and is_light:
        return CUT_MESSAGE if battery_count >= 2 else NOT_CUT_MESSAGE

    if is_blue and is_star and is_light:
        return CUT_MESSAGE if has_parallel else NOT_CUT_MESSAGE

    if is_red and is_blue:
        return CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE

    if is_red and is_star:
        return CUT_MESSAGE

    if is_red and is_light:
        return CUT_MESSAGE if battery_count >= 2 else NOT_CUT_MESSAGE

    if is_blue and is_star:
        return NOT_CUT_MESSAGE

    if is_blue and is_light:
        return CUT_MESSAGE if has_parallel else NOT_CUT_MESSAGE

    if is_star and is_light:
        return CUT_MESSAGE if battery_count >= 2 else NOT_CUT_MESSAGE

    if is_star:
        return CUT_MESSAGE

    if is_light:
        return NOT_CUT_MESSAGE

    if is_red:
        return CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE

    if is_blue:
        return CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE

    return CUT_MESSAGE
