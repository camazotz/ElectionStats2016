__author__ = 'nav'

import pandas as pd

with open("primary_results.csv") as f:
    results_lines = f.readlines()

results_table = []
firstline = True
for line in results_lines:
    strippedLine = line.strip('\n')
    if firstline:
        firstline = False
        continue
    results_table.append(strippedLine.split(","))

stateInd = 0
countyInd = 2
candInd = 5
voteInd = 6
voteFracInd = 7

'''wholeData = pd.read_csv("primary_results.csv", header=0, delimiter=",", quoting=3)
print(wholeData.shape)
print(wholeData.columns.values)
#print(wholeData["state"])
print(wholeData.loc[0][1])'''

countyDict = dict()

for row in results_table:
    if (row[countyInd].lower(),row[stateInd].lower()) not in countyDict:
        countyDict[row[countyInd].lower(), row[stateInd].lower()] = {}
        countyDict[row[countyInd].lower(), row[stateInd].lower()][row[candInd].lower()] = int(row[voteInd])
    else:
        countyDict[row[countyInd].lower(),row[stateInd].lower()][row[candInd].lower()] = int(row[voteInd])

print(countyDict['Autauga'.lower(),'Alabama'.lower()])
stateDict = dict()

for key,value in countyDict.items():
    if key[1] not in stateDict:
        stateDict[key[1]] = {}
        #print(value)
        for valKey,valValue in value.items():
            stateDict[key[1]][valKey] = int(valValue)
    else:
        for valKey, valValue in value.items():
            if valKey not in stateDict[key[1]]:
                stateDict[key[1]][valKey] = int(valValue)
            else:
                stateDict[key[1]][valKey] = stateDict[key[1]][valKey] + int(valValue)


#print(stateDict)
candidateDict = dict()
for row in results_table:
    if row[candInd] not in candidateDict:
        candidateDict[row[candInd]] = {}
        for key, value in stateDict.items():
            #print(key)
            if row[candInd] not in value:
                candidateDict[row[candInd]][key] = 0
            else:
                candidateDict[row[candInd]][key] = int(value[row[candInd]])
    else:
        for key, value in stateDict.items():
            #print(key)
            if row[candInd] not in value:
                candidateDict[row[candInd]][key] = 0
            else:
                candidateDict[row[candInd]][key] = int(value[row[candInd]])

def candidateChart(candidateName):
    maxVal = max(candidateDict[candidateName].values())
    for keys,values in candidateDict[candidateName].items():
        numAst = int(round((int(values)*10)/maxVal))        # Scale votes by a factor of 10
        print(format(keys, '<30'),end='')
        while numAst > 0:
            print('*',end='')
            numAst -= 1
        print('')

def countyChart(countyName, stateName):
    maxVal = int(max(countyDict[countyName,stateName].values()))
    for keys,values in countyDict[countyName,stateName].items():
        numAst = int(round((int(values)*10)/maxVal))        # Scale votes by a factor of 10
        print(format(keys, '<30'),end='')
        while numAst > 0:
            print('*',end='')
            numAst -= 1
        print('')

def stateChart(stateName):
    maxVal = int(max(stateDict[stateName].values()))
    for keys,values in stateDict[stateName].items():
        numAst = int(round((int(values)*10)/maxVal))        # Scale votes by a factor of 10
        print(format(keys, '<30'),end='')
        while numAst > 0:
            print('*',end='')
            numAst -= 1
        print('')

def countyCheck():
    aCounty = input('\nPlease enter county name: ')
    aState = input('Please enter state of the county: ')

    while (aCounty, aState) not in countyDict:
        print('\nInvalid county\\state combination. Please try again.')
        aCounty = input('\nPlease enter county name: ')
        aState = input('Please enter state of the county: ')

    return (aCounty, aState)

def candCountyVoting(countyName, stateName, candName):
    countyResults = countyDict[countyName,stateName]
    candFound = False
    for element in countyResults:
        if element[0] == candName:
            print(candName, ' has ', element[1], ' votes in ', countyName, ', ', stateName, sep='')
            candFound = True

    if candFound is False:
        print(countyName, ', ', stateName, ' has no voting information for ', candName, sep='')

def stateCheck():
    stateName = input('\nPlease enter state name: ')

    while stateName not in stateDict:
        print('\nInvalid state name. Please try again.')
        stateName = input('Please enter state name: ')

    return stateName

def candStateVoting(stateName, candName):
    stateResults = stateDict[stateName]
    if candName in stateResults:
        print(candName, ' has ', stateResults[candName], ' votes in ', stateName, sep='')
    else:
        print(stateName, ' has no voting information for ', candName, sep='')


#print(candidateDict)
print('Election result querying system')
print('Enter \'help\' at any of the mode menus to be directed to the guidelines on using this system')
print('Enter \'exit\' at any of the mode menus to quit the program')
'''
while (True):
    print('\nModes:')
    print('\t3 - Query by state')
    print('\t2 - Query by county')
    print('\t1 - Query by candidate')

    # Main mode error checking
    mode = input('Select mode: ')
    try:
        mode = int(mode)
    except ValueError:
        mode = mode
    while (isinstance(mode, int) is False) or mode != 1 and mode != 2 and mode != 3:
        print('\nInvalid mode. Please try again.')
        mode = input('Select mode: ')
        try:
            mode = int(mode)
        except ValueError:
            mode = mode

    # Candidate Mode
    if mode == 1:
        print('\nCandidate mode!')
        candName = input('Please enter the first and last name of a candidate: ')
        while candName not in candidateDict:
            print('\nInvalid candidate name. Please try again.')
            candName = input('Please enter the first and last name of a candidate: ')

        print('\n', candName, ' currently has ', candidateDict[candName], ' votes')

        print('\nCandidate mode options:')
        print('\t3 - Return to main menu')
        print('\t2 - State information for candidate')
        print('\t1 - County information for candidate')

        # Candidate mode error checking
        candMode = input('Select mode: ')
        try:
            candMode = int(candMode)
        except ValueError:
            candMode = candMode
        while (isinstance(candMode, int) is False) or candMode != 1 and \
                        candMode != 2 and candMode != 3:
            print('\nInvalid mode. Please try again.')
            candMode = input('Select mode: ')
            try:
                candMode = int(candMode)
            except ValueError:
                candMode = candMode

        # County information for candidate
        if candMode == 1:
            countyName, stateName = countyCheck()
            candCountyVoting(countyName, stateName)

        # State information for candidate
        elif candMode == 2:
            stateName = stateCheck()
            candStateVoting(stateName)

        # Return to main menu
        elif candMode == 3:
            continue

    elif mode == 2:
        print('County mode!')
        countyName = input('\nPlease enter county name: ')
        stateName = input('Please enter state of the county: ')

        while (countyName, stateName) not in countyDict:
            print('\nInvalid county\\state combination. Please try again.')
            countyName = input('\nPlease enter county name: ')
            stateName = input('Please enter state of the county: ')

'''





