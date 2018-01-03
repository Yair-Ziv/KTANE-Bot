"""
This is a solver for the button module.
"""
def defuse(batteries, car_indicator, freak_indicator):
    """
    Defuses the button modules
    """
    color, text = raw_input("What is the color and text of the button?\n").split(' ')
    
    if batteries > 1 and text == 'detonate':
        print 'press and release immediately'
        return
    elif batteries > 2 and freak_indicator:
        print 'press and release immediately'
        return
    elif color == 'red' and text == 'hold':
        print 'press and release immediately'
        return

    strip_indicator = raw_input('What is the color of the strip indicator?\n')
    if strip_indicator == 'blue':
        print 'Release when timer has a 4'
    elif strip_indicator == 'yellow':
        print 'Release when timer has a 5'
    else:
        print 'Release when timer has a 1'
