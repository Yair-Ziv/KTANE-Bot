"""
Solves the Simon Says module
Requires: Amount of strikes, serial number has a vowel.
"""

def defuse(strikes, is_vowel):
    """
    Main function for the Simon Says module defusion
    """
    if strikes == 0:
        strikes_0(is_vowel)
        return
    
    if strikes == 1:
        strikes_1(is_vowel)
        return
    
    if strikes == 2:
        strikes_2(is_vowel)
        return

def strikes_0(is_vowel):
    """
    Solve in case there are no strikes
    """
    sequence = raw_input('Enter sequence:\n').replace(' ', '').split(',')
    output = ''
    if is_vowel:
        for color in sequence:
            if color == 'red':
                output += 'blue '
            elif color == 'blue':
                output += 'red '
            elif color == 'yellow':
                output += 'green '
            elif color == 'green':
                output += 'yellow '
    else:
        for color in sequence:
            if color == 'red':
                output += 'blue '
            elif color == 'blue':
                output += 'yellow '
            elif color == 'yellow':
                output += 'blue '
            elif color == 'green':
                output += 'green '

    print output

def strikes_1(is_vowel):
    """
    Solve for case where there is one strike
    """
    sequence = raw_input('Enter sequence:\n').replace(' ', '').split(',')
    output = ''
    if is_vowel:
        for color in sequence:
            if color == 'red':
                output += 'yellow '
            elif color == 'blue':
                output += 'green '
            elif color == 'yellow':
                output += 'red '
            elif color == 'green':
                output += 'blue '
    else:
        for color in sequence:
            if color == 'red':
                output += 'red '
            elif color == 'blue':
                output += 'blue '
            elif color == 'yellow':
                output += 'green '
            elif color == 'green':
                output += 'yellow '

    print output

def strikes_2(is_vowel):
    """
    Solve for case of 2 strikes
    """
    sequence = raw_input('Enter sequence:\n').replace(' ', '').split(',')
    output = ''
    if is_vowel:
        for color in sequence:
            if color == 'red':
                output += 'green '
            elif color == 'blue':
                output += 'red '
            elif color == 'yellow':
                output += 'blue '
            elif color == 'green':
                output += 'yellow '
    else:
        for color in sequence:
            if color == 'red':
                output += 'yellow '
            elif color == 'blue':
                output += 'green '
            elif color == 'yellow':
                output += 'red '
            elif color == 'green':
                output += 'blue '

    print output
