from lab03 import integerDivision
from lab03 import collectEvenInts
from lab03 import countVowels
from lab03 import reverseString
from lab03 import removeSubString
def test_integerDivision():
    assert integerDivision(2,5) == 0
    assert integerDivision(10,4) == 2
    assert integerDivision(12,9) == 1
    assert integerDivision(20, 7) == 2

def test_collectEvenInts():
    a = [1,2,2,3,4,6]
    b = [2,4,4,6,8,12]
    c2 = [4,5,5,7,8,8,9]
    r = [10,12,11,13]
    assert collectEvenInts(a) == [2,2,4,6]
    assert collectEvenInts(b) == [2,4,4,6,8,12]
    assert collectEvenInts(c2) == [4,8,8]
    assert collectEvenInts(r) == [10,12]

def test_countVowels():
    c = "I Love CS9!"
    c5 = "Apple Juice"
    d = "AEIOUaeiou"
    w = "ACADEMIC"
    assert countVowels(c) == 3
    assert countVowels(d) == 10
    assert countVowels(c5) == 5
    assert countVowels(w) == 4

def test_reverseString():
    d2 = "CS9"
    d3 = "UCSB"
    d9 = "Grape"
    j = "Mango"
    assert reverseString(d2) == "9SC"
    assert reverseString(d3) == "BSCU"
    assert reverseString(d9) == "eparG"
    assert reverseString(j) == "ognaM"

def test_removeSubString():
    a2 = "CSCSCCCCS"
    d4 = "CS"
    d5 = "CCC"
    ch = "C"
    assert removeSubString(a2, d4) == "CCC"
    assert removeSubString(a2, d5) == "CSCSCS"
    assert removeSubString(d4, ch) == "S"
    assert removeSubString(a2, ch) == "SSS"











