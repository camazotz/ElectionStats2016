__author__ = 'nav'


stateInd, countyInd, candInd, voteInd, partyInd = (0, 0, 0, 0, 0)

# Dataset name validation and opening
def addDataset():
    userDataset = ''
    results_lines = []
    while True:
        try:
            userDataset = input('Please enter a dataset: ')

            with open(userDataset) as f:
                results_lines = f.readlines()
        except:
            print('Incorrect dataset. Please try again.')
            continue

        break

    return results_lines

# Input validation for indices inputted
def indModeCheck():
    mode = input('Select mode: ').strip()
    try:
        mode = int(mode)
    except ValueError:
        mode = mode
    while (isinstance(mode, int) is False) or mode != 1 and mode != 2:
        print('\nInvalid mode. Please try again.')
        mode = input('Select mode: ').strip()
        try:
            mode = int(mode)
        except ValueError:
            mode = mode

    return mode

# Input validation for field indices
def fieldIndCheck(field):
    mode = input('Please enter the index for ' + field+ ': ').strip()
    try:
        mode = int(mode)
    except ValueError:
        mode = mode
    while (isinstance(mode, int) is False):
        print('\nInvalid index. Please try again.')
        mode = input('Please enter the index for ' + field + ': ').strip()
        try:
            mode = int(mode)
        except ValueError:
            mode = mode

    return mode

# Setting fields for various columns in dataset
def setFields():
    newStateInd = fieldIndCheck('state')
    newCountyInd = fieldIndCheck('county')
    newCandInd = fieldIndCheck('candidate')
    newVoteInd = fieldIndCheck('vote')
    newPartyInd = fieldIndCheck('party')

    return newStateInd, newCountyInd, newCandInd, newVoteInd, newPartyInd

def setIndices():
    global stateInd, countyInd, candInd, voteInd, partyInd
    print('You have the option to set indices for the fields in the dataset or use the default fields.')
    print('Would you like to set your own fields?')
    print('\t1 - Yes')
    print('\t2 - No')
    indMode = indModeCheck()
    if indMode == 1:
        stateInd, countyInd, candInd, voteInd, partyInd = setFields()
    elif indMode == 2:
        stateInd = 0
        countyInd = 2
        candInd = 5
        voteInd = 6
        partyInd = 4

    return stateInd, countyInd, candInd, voteInd, partyInd

# Return a table of dataset
def getTable(results_lines):
    results_table = []
    firstline = True
    for line in results_lines:
        strippedLine = line.strip('\n')
        if firstline:
            firstline = False
            continue
        results_table.append(strippedLine.split(","))

    return results_table
