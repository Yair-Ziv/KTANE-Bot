"""
Solver for the keypad module
"""
#Current symbol names for testing, if after speech recognition some words don't work they 
#will be changed
#TODO Check the words in speech recognition
#TODO Find efficiant way to solve the problem
columns = [
    ['balloon', 'tennis', 'eighty', 'lambda', 'lightning', 'spaceship', 'h', 'house', 'see'],
    ['e', 'echo', 'balloon', 'tennis', 'see', 'o', 'oscar', 'star', 'h', 'hotel', 'question'],
    ['copyright', 'torso', 'waist', 'o', 'oscar', 'k', 'kilo', 'r', 'romeo', 'lambda', 'star'],
    ['six', 'paragraph', 'tibby', 'spaceship', 'k', 'kilo', 'question', 'smiley'],
    ['psi', 'menorah', 'smiley', 'tibby', 'see', 'paragraph', 'snake', 'star'],
    ['six', 'e', 'echo', 'equals', 'aerobics', 'psi', 'menorah', 'n', 'november', 'omega']
]

def defuse():
    """
    Main defusal function
    """
    sequence = raw_input('Enter the sequence:\n').split(' ')
    correct_column = -1

    if len(sequence) != 4:
        return defuse()

    for index, column in enumerate(columns):
        if sequence[0] in column:
            if sequence[1] in column:
                if sequence[2] in column:
                    if sequence[3] in column:
                        correct_column = index

    positions = []
    for value in sequence:
        positions.append(columns[correct_column].index(value))

    positions.sort()

    for position in positions:
        print '{},'.format(columns[correct_column][position]),
