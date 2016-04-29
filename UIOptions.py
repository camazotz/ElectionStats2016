__author__ = 'nav'

# Mode checking for each menu, goes up to a default of 5 options for each menu and must be an integer
def modeCheck():
    mode = input('Select mode: ').strip()
    try:
        mode = int(mode)
    except ValueError:
        mode = mode
    while (isinstance(mode, int) is False) or mode != 1 and mode != 2 and mode != 3\
            and mode != 4 and mode != 5:
        print('\nInvalid mode. Please try again.')
        mode = input('Select mode: ').strip()
        try:
            mode = int(mode)
        except ValueError:
            mode = mode

    return mode

def helpInstructions():
    print('\nYou may select from one of three modes: State, county, and candidate.')
    print('Each mode presents an option menu to view its information in relation to the other modes.')
    print('When selected, each mode will initially output a bar graph showing the number of votes'
          ' as a function of another mode.')
    print('The number of votes is scaled to 10. So 10 asterisks on the bar graph for any variable'
          ' indicates that the variable has the highest number of votes in that function.')
    print('So for example, if you select candidate mode, you will initially see a bar graph of '
          'the number of votes the candidate has garnered from each state. '
          '\nThe state with 10 asterisks next to it is the state from which the candidate has earned'
          ' the most votes.'
          '\nAnd then you have the option to see the candidate\'s'
          ' voting information for a given state or a given county (which is supplied by the user).')
    print('You may re-enter this help menu by inputting the appropriate option at any of the mode menus.')
    print('You may exit the program at any of mode menus by inputting the appropriate option.')