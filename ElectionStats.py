__author__ = 'nav'

import pandas as pd
import sys

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

#print(countyDict['Autauga'.lower(),'Alabama'.lower()])
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
    if row[candInd].lower() not in candidateDict:
        candidateDict[row[candInd].lower()] = {}
        for key, value in stateDict.items():
            #print(key)
            if row[candInd].lower() not in value:
                candidateDict[row[candInd].lower()][key] = 0
            else:
                candidateDict[row[candInd].lower()][key] = int(value[row[candInd].lower()])
    else:
        for key, value in stateDict.items():
            #print(key)
            if row[candInd].lower() not in value:
                candidateDict[row[candInd].lower()][key] = 0
            else:
                candidateDict[row[candInd].lower()][key] = int(value[row[candInd].lower()])

#print(candidateDict);

def candidateChart(candidateName):
    maxVal = max(candidateDict[candidateName].values())

    for keys,values in candidateDict[candidateName].items():
        numAst = int(round((int(values)*10)/maxVal))        # Scale votes by a factor of 10
        print(format(keys.title(), '<30'),end='')
        while numAst > 0:
            print('*',end='')
            numAst -= 1
        print('')

def countyChart(countyName, stateName):
    maxVal = int(max(countyDict[countyName,stateName].values()))

    for keys,values in countyDict[countyName,stateName].items():
        numAst = int(round((int(values)*10)/maxVal))        # Scale votes by a factor of 10
        print(format(keys.title(), '<30'),end='')
        while numAst > 0:
            print('*',end='')
            numAst -= 1
        print('')

def stateChart(stateName):
    maxVal = int(max(stateDict[stateName].values()))

    for keys,values in stateDict[stateName].items():
        numAst = int(round((int(values)*10)/maxVal))        # Scale votes by a factor of 10
        print(format(keys.title(), '<30'),end='')
        while numAst > 0:
            print('*',end='')
            numAst -= 1
        print('')

def countyCheck():
    aCounty = input('\nPlease enter county name: ').strip().lower()
    aState = input('Please enter state of the county: ').strip().lower()

    while (aCounty, aState) not in countyDict:
        print('\nInvalid county\\state combination. Please try again.')
        aCounty = input('\nPlease enter county name: ').strip().lower()
        aState = input('Please enter state of the county: ').strip().lower()

    return (aCounty, aState)

def stateCheck():
    stateName = input('\nPlease enter state name: ').strip().lower()

    while stateName not in stateDict:
        print('\nInvalid state name. Please try again.')
        stateName = input('Please enter state name: ').strip().lower()

    return stateName

def candCheck():
    candName = input('\nPlease enter candidate name: ').strip().lower()

    while candName not in candidateDict:
        print('\nInvalid candidate name. Please try again.')
        candName = input('Please enter candidate name: ').strip().lower()

    return candName

def candCountyVoting(countyName, stateName, candName):
    #print(countyDict[countyName,stateName])
    if candName in countyDict[countyName,stateName]:
        print(candName.title(), ' has ', countyDict[countyName,stateName][candName], ' votes in ',
              countyName.title(), ', ', stateName.title(), sep='')
    else:
        print(countyName.title(), ', ', stateName.title(), ' has no voting information for ', candName.title(), sep='')

def candStateVoting(stateName, candName):
    stateResults = stateDict[stateName]
    if candName in stateResults:
        print(candName.title(), ' has ', stateResults[candName], ' votes in ', stateName.title(), sep='')
    else:
        print(stateName.title(), ' has no voting information for ', candName.title(), sep='')


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

#print(candidateDict)
print('Election result querying system')
print('Enter \'help\' at any of the mode menus to be directed to the guidelines on using this system')
print('Enter \'exit\' at any of the mode menus to quit the program')

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
        candName = input('Please enter the first and last name of a candidate: ').strip().lower()
        while candName not in candidateDict:
            print('\nInvalid candidate name. Please try again.')
            candName = input('Please enter the first and last name of a candidate: ').strip().lower()

        candVotes = sum(candidateDict[candName].values())       # Total votes for candidate
        print('\n', candName.title(), ' currently has ', candVotes, ' votes\n', sep='')

        candidateChart(candName)

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
                countyName, stateName = countyCheck()
                candCountyVoting(countyName, stateName, candName)

            # State information for candidate
            elif candMode == 2:
                stateName = stateCheck()
                candStateVoting(stateName, candName)

            # Return to main menu
            elif candMode == 3:
                break

            elif candMode == 4:
                print('Help items')

            elif candMode == 5:
                sys.exit()

    # County mode
    elif mode == 2:
        print('County mode!')
        countyName = input('\nPlease enter county name: ').strip().lower()
        stateName = input('Please enter state of the county: ').strip().lower()

        while (countyName, stateName) not in countyDict:
            print('\nInvalid county\\state combination. Please try again.')
            countyName = input('\nPlease enter county name: ').strip().lower()
            stateName = input('Please enter state of the county: ').strip().lower()


        countyChart(countyName, stateName)

        while (True):
            print('\nCounty mode options:')
            print('\t5 - Quit')
            print('\t4 - Help')
            print('\t3 - Return to main menu')
            print('\t2 - State information for county')
            print('\t1 - Candidate information for county')

            # County mode error checking
            countyMode = modeCheck()


            # Candidate information for county
            if countyMode == 1:
                candName = candCheck()
                candCountyVoting(countyName, stateName, candName)

            # State information for county
            elif countyMode == 2:
                print('some fraction')

            # Return to main menu
            elif countyMode == 3:
                break

            elif countyMode == 4:
                print('Help items')

            elif countyMode == 5:
                sys.exit()


    elif mode == 4:
        print('Help items')

    elif mode == 5:
        sys.exit()





