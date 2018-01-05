"""
Complicated Wires solver
Requires: Last digit of the serial, has a parallel port, battert count
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
    is_battery_count = battery_count >= 2

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

    binary_representation = ''
    binary_representation += '1' if is_red else '0'
    binary_representation += '1' if is_blue else '0'
    binary_representation += '1' if is_light else '0'
    binary_representation += '1' if is_star else '0'

    decimal_value = int(binary_representation, 2)
    return {
        0:CUT_MESSAGE,
        1:CUT_MESSAGE,
        2:NOT_CUT_MESSAGE,
        3:CUT_MESSAGE if is_battery_count else NOT_CUT_MESSAGE,
        4:CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE,
        5:NOT_CUT_MESSAGE,
        6:CUT_MESSAGE if has_parallel else NOT_CUT_MESSAGE,
        7:CUT_MESSAGE if has_parallel else NOT_CUT_MESSAGE,
        8:CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE,
        9:CUT_MESSAGE,
        10:CUT_MESSAGE if is_battery_count else NOT_CUT_MESSAGE,
        11:CUT_MESSAGE if is_battery_count else NOT_CUT_MESSAGE,
        12:CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE,
        13:CUT_MESSAGE if has_parallel else NOT_CUT_MESSAGE,
        14:CUT_MESSAGE if last_digit_even else NOT_CUT_MESSAGE,
        15:NOT_CUT_MESSAGE
    }[decimal_value]
    """
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
    """
