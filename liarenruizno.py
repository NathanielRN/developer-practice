def getLowerAndUpperBound(classSize, surveyMatrix):
	lower = 0
	upper = 0
	minimumLowerBound = None
	foundAParadox = 0

	for studentNum in range(classSize):			
		studentIsTruthTeller = True

		for peer in range(classSize):
			if not studentIsTruthTeller:
				break
				
			if surveyMatrix[studentNum][peer] == 'T':
				for i in range(classSize):
					if surveyMatrix[peer][i] != surveyMatrix[studentNum][i]:
						studentIsTruthTeller = False
						break
			else:
				everyoneIsALiar = True
				for i in range(classSize):
					if surveyMatrix[peer][i] != surveyMatrix[studentNum][i]:
						break
					elif surveyMatrix[studentNum][i] == 'T':
						everyoneIsALiar = False
				else:
					if not everyoneIsALiar:
						studentIsTruthTeller = False
						break

		if studentIsTruthTeller and surveyMatrix[studentNum][studentNum] == 'L':
			foundAParadox += 1
			continue
			
		if not studentIsTruthTeller:
			lower += 1
			upper += 1
		else:
			truthTellerLiars = len([liar for liar in surveyMatrix[studentNum] if liar == 'L'])
			minimumLowerBound = truthTellerLiars if (minimumLowerBound == None or truthTellerLiars < minimumLowerBound) else minimumLowerBound
			upper += 1
	
	if minimumLowerBound != None:
		lower = minimumLowerBound
	elif foundAParadox > 0:
		return -1, -1
	
	return (lower, upper)

def classroomPrinter(roomNum, message, shouldAddNewLine):
	if shouldAddNewLine:
		print('Class Room#' + str(roomNum) + ' ' + message, end="")
	else:
		print('Class Room#' + str(roomNum) + ' ' + message)

def main():
	numberOfTestCases = eval(input())
	for index in range(numberOfTestCases):
		classSize = eval(input())
		surveyMatrix = []
		
		for i in range(classSize):
			characters = []
			for inputCharacter in input():
				characters += inputCharacter
			surveyMatrix.append(characters)
 
		lower, upper = getLowerAndUpperBound(classSize, surveyMatrix)
 
		if lower == -1:
			classroomPrinter(index+1, "is paradoxical", index == numberOfTestCases-1)
		else:
			classroomPrinter(index+1, "contains atleast " + str(lower) + " and atmost " + str(upper) + " liars", index == numberOfTestCases-1)
			
main()			
