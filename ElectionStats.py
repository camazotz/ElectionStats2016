__author__ = 'nav'

import sys
from dataConfiguration import *
from dictOperations import *
from UIOptions import *

# Takes a user-specified dataset
results_lines = addDataset()

results_table = getTable(results_lines)     # Creates a table out of the data

# Takes user-specified indices for the data or goes with the default indices
stateInd, countyInd, candInd, voteInd, partyInd = setIndices()

# Creates the required dictionaries from the data
createDicts(stateInd, countyInd, candInd, voteInd, partyInd, results_table)

# User interface system
print('Election result querying system')
print('Enter \'help\' at any of the mode menus to be directed to the guidelines on using this system')
print('Enter \'exit\' at any of the mode menus to quit the program')

# Loop until user exits
while (True):
    print('\nModes:')
    print('\t5 - Quit')
    print('\t4 - Help')
    print('\t3 - Query by state')
    print('\t2 - Query by county')
    print('\t1 - Query by candidate')

    # Main mode error checking
    mode = modeCheck()


    # Candidate Mode
    if mode == 1:
        print('\nCandidate mode!')

        # Error checking candidate name
        candName = input('Please enter the first and last name of a candidate: ').strip().lower()
        while candName not in candidateDict:
            print('\nInvalid candidate name. Please try again.')
            candName = input('Please enter the first and last name of a candidate: ').strip().lower()

        candVotes = sum(candidateDict[candName].values())       # Total votes for candidate
        print('\n', candName.title(), ' currently has ', candVotes, ' votes\n', sep='')

        candidateChart(candName)        # Print a bar graph of candidate votes per state

        # Options for each candidate
        while (True):
            print('\nCandidate mode options:')
            print('\t5 - Quit')
            print('\t4 - Help')
            print('\t3 - Return to main menu')
            print('\t2 - State information for candidate')
            print('\t1 - County information for candidate')

            # Candidate mode error checking
            candMode = modeCheck()


            # County information for candidate
            if candMode == 1:
                countyName, stateName = countyCandCheck()
                candCountyVoting(countyName, stateName, candName)

            # State information for candidate
            elif candMode == 2:
                stateName = stateCheck()
                candStateVoting(stateName, candName)

            # Return to main menu
            elif candMode == 3:
                break

            elif candMode == 4:
                helpInstructions()

            elif candMode == 5:
                sys.exit()

    # County mode
    elif mode == 2:
        print('\nCounty mode!')
        countyName = input('Please enter county name: ').strip().lower()
        stateName = input('Please enter state of the county: ').strip().lower()

        # Error checking for county and state name
        while (countyName, stateName) not in countyDict:
            print('\nInvalid county\\state combination. Please try again.')
            countyName = input('\nPlease enter county name: ').strip().lower()
            stateName = input('Please enter state of the county: ').strip().lower()


        countyChart(countyName, stateName)      # Create a bar graph for county/candidate votes

        # County mode options
        while (True):
            print('\nCounty mode options:')
            print('\t5 - Quit')
            print('\t4 - Help')
            print('\t3 - Return to main menu')
            print('\t2 - State information for county')
            print('\t1 - Party information for county')

            # County mode error checking
            countyMode = modeCheck()


            # Party information for county
            if countyMode == 1:
                aParty = partyCheck()
                countyPartyVoting(countyName, stateName, aParty)

            # State information for county
            elif countyMode == 2:
                countyStateVoting(countyName, stateName)

            # Return to main menu
            elif countyMode == 3:
                break

            # Help
            elif countyMode == 4:
                helpInstructions()

            # Quit
            elif countyMode == 5:
                sys.exit()

    # State mode
    elif mode == 3:
        print('\nState mode!')
        stateName = input('Please enter state of the county: ').strip().lower()

        # Error checking for state name
        while stateName not in stateDict:
            print('\nInvalid state name. Please try again.')
            stateName = input('Please enter the name of a state: ').strip().lower()

        stateChart(stateName)       # Bar graph showing state/candidate votes

        # State mode options loop
        while (True):
            print('\nState mode options:')
            print('\t5 - Quit')
            print('\t4 - Help')
            print('\t3 - Return to main menu')
            print('\t2 - County information for state')
            print('\t1 - Party information for state')

            stateMode = modeCheck()     # Checks whether mode is correctly entered

            # Party information for state
            if stateMode == 1:
                partyName = partyCheck()
                statePartyCheck(stateName, partyName)

            # County information for state
            elif stateMode == 2:
                aCounty = countyCheck(stateName)
                countyStateVoting(aCounty, stateName)

            # Return to main menu
            elif stateMode == 3:
                break

            # Help menu
            elif stateMode == 4:
                helpInstructions()

            # Exit
            elif stateMode == 5:
                sys.exit()

    # Help menu
    elif mode == 4:
        helpInstructions()

    # Exit program
    elif mode == 5:
        sys.exit()
