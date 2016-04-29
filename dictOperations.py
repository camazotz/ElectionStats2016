__author__ = 'nav'

from dictCreation import *

# The names of each method indicate which two variables/factors are being compared

# County/State voting
def countyStateVoting(countyName, stateName):
    stateVotes = sum(statePartyDict[stateName].values())
    countyVotes = sum(countyPartyDict[countyName, stateName].values())

    countyFrac = countyVotes / stateVotes
    countyFrac = countyFrac * 100
    countyPercent = round(countyFrac, 2)

    print(countyName.title(), ' county has ', countyPercent, '% of the votes in ', stateName.title(), sep='')

# Charts for candidate, county, state
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

# Input validation for county, state, party and candidate
def countyCandCheck():
    aCounty = input('\nPlease enter county name: ').strip().lower()
    aState = input('Please enter state of the county: ').strip().lower()

    while (aCounty, aState) not in countyDict:
        print('\nInvalid county\\state combination. Please try again.')
        aCounty = input('\nPlease enter county name: ').strip().lower()
        aState = input('Please enter state of the county: ').strip().lower()

    return (aCounty, aState)

def countyCheck(stateName):
    aCounty = input('\nPlease enter county name: ').strip().lower()

    while (aCounty, stateName) not in countyDict:
        print('\nInvalid county\\state combination. Please try again.')
        aCounty = input('\nPlease enter county name: ').strip().lower()

    return aCounty

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

def partyCheck():
    partyName = input('\nPlease enter party name: ').strip().lower()
    partyTypes = ['democratic', 'democrat', 'republican']
    while partyName not in partyTypes:
        print('\nInvalid party name. Please try again.')
        partyName = input('Please enter party name: ').strip().lower()

    if partyName == partyTypes[0]:
        partyName = 'democrat'

    return partyName


# County/Party voting
def countyPartyVoting(countyName, stateName, partyName):
    if partyName not in countyPartyDict[countyName, stateName]:
        print(countyName.title(), ', ', stateName.title(), ' has no voting information for ', partyName.title(), ' party', sep='')
    else:
        print(partyName.title(), ' has ', countyPartyDict[countyName, stateName][partyName], ' votes in ',
              countyName.title(), ', ', stateName.title(), sep='')

# Check if state has voting information for a given party
def statePartyCheck(stateName, partyName):
    if partyName not in statePartyDict[stateName]:
        print(stateName.title(), ' has no voting information for ', partyName.title(), ' party', sep='')
    else:
        print(partyName.title(), ' has ', statePartyDict[stateName][partyName], ' votes in ',
              stateName.title(), sep='')

# Check if county has voting information for candidate
def candCountyVoting(countyName, stateName, candName):
    #print(countyDict[countyName,stateName])
    if candName in countyDict[countyName,stateName]:
        print(candName.title(), ' has ', countyDict[countyName,stateName][candName], ' votes in ',
              countyName.title(), ', ', stateName.title(), sep='')
    else:
        print(countyName.title(), ', ', stateName.title(), ' has no voting information for ', candName.title(), sep='')

# Check if state has voting information for candidate
def candStateVoting(stateName, candName):
    stateResults = stateDict[stateName]
    if candName in stateResults:
        print(candName.title(), ' has ', stateResults[candName], ' votes in ', stateName.title(), sep='')
    else:
        print(stateName.title(), ' has no voting information for ', candName.title(), sep='')