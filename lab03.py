
def integerDivision(n, k):
    if n < k:
        return 0
    else:
        return 1 + integerDivision(n - k, k)


def collectEvenInts(listOfInt):
    if not listOfInt:
        return []
    elif listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    else:
        return collectEvenInts(listOfInt[1:])

def countVowels(someString):
   if not someString:
       return 0
   elif someString[0].lower() in 'aeiou':
       return 1 + countVowels(someString[1:])
   else:
       return countVowels(someString[1:])

def reverseString(s):
    if len(s) == 0:
        return s
    else:
        return reverseString(s[1:]) + s[0]

def removeSubString(s, sub):
    sub_len = len(sub)

    if len(s) < sub_len:
        return s
    elif s[:sub_len] == sub:
        return removeSubString(s[sub_len:], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)











