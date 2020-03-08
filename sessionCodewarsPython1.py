# TL : 26-02-2020.


import math

#####1#####
#A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
#In this Kata, we will restrict ourselves to decimal (base 10).
#Write a function that returns True if the given number is narcissistic.

def narcissistic( value ):
	finalSum = 0
	power = len(str(value)) # The value's number of digits.
	arrayOfDigits = list(str(value)) # Splits the number to get each number separated in a list.
	for x in arrayOfDigits:
		finalSum += int(x)**power
	return finalSum == value


#####2#####
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
	text = text.lower() # Avoids case problems.
	alreadyTestedChar = [] # Avoids the count of repetitions.
	countDistinct = 0
	for char in text:
		count = 0
		for char2 in text:
			if char == char2 and char not in alreadyTestedChar:
				count += 1
		if count > 1:
			countDistinct += 1
		alreadyTestedChar.append(char)
	return countDistinct


	

###3###
#Given an integral number, determine if it's a square number:
#In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself.

def is_square(n): 
	if n < 0: # Avoids the sqrt function to crash.
		return False
	sqroot = math.sqrt(n) # Always a float.
	if (int(sqroot) ** 2 == n): # If the returned float isn't a round number, then the given number isn't a perfect square. The convertion into an integer will make us lose some decimals, and then the result multiplied by itself wouldn't give the start number.
		return True
	return False

	###BEST SOLUCE###
	#import math
	#def is_square(n):
    	#return n > -1 and math.sqrt(n) % 1 == 0 A float number % 1 will never be equal to 0.



###4###
#Given an array, find the integer that appears an odd number of times.
def find_it(seq):
	for x in seq:
		if seq.count(x) % 2 == 1:
			return x


###5###
#Return the first longest string consisting of k consecutive strings taken in the array.
def longest_consec(strarr, k):
	maxString=""
	if (len(strarr) == 0) or (k > len(strarr)) or (k <= 0):
		return maxString
	for x in range(0,len(strarr)):
		testedString = strarr[x] # Current word.
		if x <= len(strarr) - k:
			for i in range(1,k): # Adding the k - 1 consecutive words.
				testedString += strarr[x+i]
		if len(testedString) > len(maxString):
			maxString = testedString
	return maxString


###6###
#ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
#ROT13 is an example of the Caesar cipher.
#Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string,
#they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13.

def rot13(message):
	newMessage = ""
	for x in message:
		if (ord(x) >= 65 and ord(x) <= 90) or (ord(x) >= 97 and ord(x) <= 122): # X between A-Z or a-z.
			if (ord(x) >= 65 and ord(x) <= 77) or (ord(x) >= 97 and ord(x) <= 109): # X before M or m.
				newMessage = newMessage + chr(ord(x) + 13)
			else:
				newMessage = newMessage + chr(ord(x) - 13)
		else:
			newMessage = newMessage + x # Other characters than letters.

	return newMessage

###7###
#Square every digit of a number.
#For example, if we run 9119 through the function, 811181 will come out

def square_digits(num):
	strNum = str(num);
	strResponse = ""
	for x in strNum:
		strResponse += str(int(x) * int(x)) # Avoids concatenation errors.
	return int(strResponse)


###8###
#In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
def filter_list(l):
	newList = []
	for x in l:
		if not isinstance(x, str): # Determines if the current element is an instance of the str class.
			newList.append(x)
	return newList


###9###
#Given an array of integers, remove the smallest value. Do not mutate the original array/list.
#If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

def remove_smallest(numbers):
	if (len(numbers) == 0):
		return []
	index = numbers.index(min(numbers)) # Gets the position of the first occurence of the lowest value in the list.
	newList = []
	for x in range(0,len(numbers)):
		if x != index:
			newList.append(numbers[x])
	return newList

###10###
#For building the encrypted string:
#Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
#Do this n times!

def decrypt(encrypted_text, n):
    treatedtext = encrypted_text
    for i in range(0, n):
    	secondsCharArray = []
    	othersCharArray = []
    	for x in range(0, len(treatedtext)):
    		if x < len(treatedtext) // 2:
    			secondsCharArray.append(treatedtext[x])
    		else:
    			othersCharArray.append(treatedtext[x])
    	treatedtext = ""
    	l = 0
    	k = 0
    	for y in range(0, len(secondsCharArray) + len(othersCharArray)):
    		if y % 2 == 1:
    			treatedtext += secondsCharArray[l]
    			l += 1
    		else:
    			treatedtext += othersCharArray[k]
    			k += 1
    return treatedtext


def encrypt(text, n):
	treatedtext = text
	for i in range(0, n):
		secondsCharArray = []
		othersCharArray = []
		for x in range(0, len(treatedtext)):
			if x % 2 == 1:
				secondsCharArray.append(treatedtext[x])
			else:
				othersCharArray.append(treatedtext[x])
		treatedtext = "".join(secondsCharArray) + "".join(othersCharArray)
	return treatedtext
