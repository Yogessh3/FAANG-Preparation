#Time - O(n) || Space - O(n)
def validAbbreviation (str, abbr):
	num = ''
	abbrevation = []
	for idx in range(len(abbr)):
		char = abbr[idx]
		num = num + char if char in '0123456789' else ''
		if idx == len(abbr) - 1 or abbr[idx+1] not in '0123456789':
			if(num != ''):
				replaceRange = int(num)
				replaceRange = 1 if replaceRange == 0 else replaceRange
				for idx in range(replaceRange):
					abbrevation.append('*')
		if char not in '0123456789':
			abbrevation.append(char)
	abbLength = len(abbrevation)
	if(abbLength != len(str)):
		return False
	for idx in range(len(abbrevation)):
		if(abbrevation[idx] != '*' and abbrevation[idx] != str[idx]):
			return False
	return True