__author__ = 'nav'

countyPartyDict = dict()
statePartyDict = dict()
countyDict = dict()
stateDict = dict()
candidateDict = dict()


def createDicts(stateInd, countyInd, candInd, voteInd, partyInd, results_table):

    # County/Party dictionary
    for row in results_table:
        if (row[countyInd].lower(), row[stateInd].lower()) not in countyPartyDict:
            countyPartyDict[row[countyInd].lower(), row[stateInd].lower()] = {}
            countyPartyDict[row[countyInd].lower(), row[stateInd].lower()][row[partyInd].lower()] = int(row[voteInd])
        else:
            if row[partyInd].lower() not in countyPartyDict[row[countyInd].lower(), row[stateInd].lower()]:
                countyPartyDict[row[countyInd].lower(), row[stateInd].lower()][row[partyInd].lower()] = int(row[voteInd])
            else:
                countyPartyDict[row[countyInd].lower(), row[stateInd].lower()][row[partyInd].lower()] += int(row[voteInd])

    # State/Party Dictionary
    for row in results_table:
        if row[stateInd].lower() not in statePartyDict:
            statePartyDict[row[stateInd].lower()] = {}
            statePartyDict[row[stateInd].lower()][row[partyInd].lower()] = int(row[voteInd])
        else:
            if row[partyInd].lower() not in statePartyDict[row[stateInd].lower()]:
                statePartyDict[row[stateInd].lower()][row[partyInd].lower()] = int(row[voteInd])
            else:
                statePartyDict[row[stateInd].lower()][row[partyInd].lower()] += int(row[voteInd])

    # County/Candidate dictionary
    for row in results_table:
        if (row[countyInd].lower(),row[stateInd].lower()) not in countyDict:
            countyDict[row[countyInd].lower(), row[stateInd].lower()] = {}
            countyDict[row[countyInd].lower(), row[stateInd].lower()][row[candInd].lower()] = int(row[voteInd])
        else:
            countyDict[row[countyInd].lower(),row[stateInd].lower()][row[candInd].lower()] = int(row[voteInd])

    # State/Candidate dictionary
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

    # Candidate dictionary
    for row in results_table:
        if row[candInd].lower() not in candidateDict:
            candidateDict[row[candInd].lower()] = {}
            for key, value in stateDict.items():
                if row[candInd].lower() not in value:
                    candidateDict[row[candInd].lower()][key] = 0
                else:
                    candidateDict[row[candInd].lower()][key] = int(value[row[candInd].lower()])
        else:
            for key, value in stateDict.items():
                if row[candInd].lower() not in value:
                    candidateDict[row[candInd].lower()][key] = 0
                else:
                    candidateDict[row[candInd].lower()][key] = int(value[row[candInd].lower()])

    #return countyPartyDict, statePartyDict, countyDict, stateDict, candidateDict
