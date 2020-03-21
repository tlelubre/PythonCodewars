# TL : 20-03-20


###1###
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    newString = string.lower() # Avoids the case.
    for x in newString:
        if newString.count(x) > 1: # Determines the number of occurences of a letter in the string.
            return False
    return True

    #BEST PRACTICE : return len(string) == len(set(string.lower()))  A set can't content duplicates.


###2###
# You are given a string of space separated numbers, and have to return the highest and lowest number (separated by a white space).
def high_and_low(numbers):
    stringList = numbers.split(" ") # Gets all the numbers.
    intList = []
    for x in stringList:
        intList.append(int(x)) # We need to get the integer version of these numbers, otherwise the max/min functions could return wrong results.
    minNum = min(intList)
    maxNum = max(intList)
    return str(maxNum) + " " + str(minNum)

    #BEST PRATICE : n = map(int, numbers.split(' ')) 
    #               return str(max(n)) + ' ' + str(min(n))


###3###
# Tribonacci.
# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
def tribonacci(signature, n):
    if (n == 1):
        return [signature[0]]
    elif (n == 2):
        return signature[0:2]
    elif (n == 3):
        return signature
    elif (n == 0):
        return []
    while(n > 3):
        signature.append(sum(signature[-3:]))
        n -= 1
    return signature

    # Recursive version : return signature[:n] if n<=len(signature) else tribonacci(signature + [sum(signature[-3:])],n)
    # Best iterative version : while len(signature) < n:
    #                               signature.append(sum(signature[-3:]))
    #                          return signature[:n]




###4###
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.
def solution(string,markers):
    newString = ""
    x = 0
    while(x < len(string)):
        if string[x] not in markers:
            newString += string[x]
        else:
            while(x < len(string) and string[x] != '\n'):
                x += 1
            newString = newString.rstrip(" ")
            if (x < len(string)):
                newString += "\n"
        x += 1
    return newString
    # Another solution : split the string on the '\n' character, then treat each element of the resulted list, and finaly join the list on the '\n' char.


###5###
# You need to write regex that will validate a password to make sure it meets the following criteria:
# At least six characters long
# Contains a lowercase letter
# Contains an uppercase letter
# Contains a number
# Valid passwords will only be alphanumeric characters.
regex = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)


