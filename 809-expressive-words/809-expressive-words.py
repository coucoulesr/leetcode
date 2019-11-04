class Solution:
	def expressiveWords(self, S, words):
		soln = 0
		sArray = self.strToCharArray(S)
		for word in words:
			wordCharArray = self.strToCharArray(word)
			print(sArray, wordCharArray)
			if self.arraysMatch(sArray, wordCharArray):
				soln += 1
		return soln			
    
	def strToCharArray(self, inStr):
		outArray = []
		storedChar = None
		idx = -1
		for ch in inStr:
			if ch == storedChar:
				outArray[idx][1] += 1
			else:
				storedChar = ch
				charArray = [storedChar, 1]
				outArray.append(charArray)
				idx += 1
		return outArray

	def arraysMatch(self, array1, array2): # Be sure to pass S (the elongated string) first
		if len(array1) == len(array2):
			i = 0
			while i < len(array1):
				if array1[i][0] == array2[i][0] and array1[i][1] >= array2[i][1]:
					if array1[i][1] >= 3 or array1[i][1] == array2[i][1]:
						i += 1
						continue
					else:
						return False
				else:
					return False
		else:
			return False
		return True








































# def romanToInt(s):
# 	conversionDict = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
# 	
# 	total = 0
# 	inList = [char for char in s.upper()]
# 	current = 0
# 	print(inList)
# 	
# 	for i in range(len(inList)):
# 		previous = current
# 		current = inList.pop()
# 		try:
# 			if previous == 0:	
# 				total += conversionDict[current]
# 			else:
# 				if (conversionDict[current] >= conversionDict[previous]):
# 					total += conversionDict[current]
# 				else:
# 					total -= conversionDict[current]
# 		except:
# 			return None
# 		
# 	return total
# 
# print(romanToInt("CDXVIII"))
# 			
