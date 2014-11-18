# Functions for students to implement.
def solveOnlyLists(inputList):
    uniqueList = []
    for i in inputList:
	if i not in uniqueList:
		uniqueList.append(i)
    #compute unique items in inputList
    return uniqueList

def solveDict(inputList):
    uniqueList = []
    dict1 = {}
    for i in inputList:
	if i not in dict1:
		dict1[i] = 1
		uniqueList.append(i)
		
    #compute unique items in inputList
    return uniqueList

def solveSorted(sortedInputList):
    uniqueList = []

    j = len(sortedInputList)
    uniqueList.append(sortedInputList[0])
    for i in xrange(1, j):		
	if sortedInputList[i - 1] != sortedInputList[i]:
		uniqueList.append(sortedInputList[i])	
    #compute unique items in inputList
    return uniqueList

