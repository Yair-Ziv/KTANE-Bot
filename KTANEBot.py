"""
This project is a bot that will be an assistant to a player playing
KTANE when he has no friends.
"""
import Modules

needed = {'batteries':None, 
          'serial port':None,
          'vowel':None,
          'serial number':None, 
          'car indicator':None,
          'freak':None}

def main():
    Modules.SimpleWires.defuse(needed['serial number'])

if __name__ == '__main__':
    main()
