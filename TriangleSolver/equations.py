from math import *

def sss(a, b, c):

    return

def twoAngle_oneSide(a, b, c, A, B, C):
    
    return


def oneAngle_twoSide(a, b, c, A, B, C):

    return


def rightTriangle(a, b, c):
    # In this case the variable 'c' is the hypotenuse
    if a == 0 and b != 0 and c != 0:
        a = sqrt(c**2 - b**2) 
    elif b == 0 and a != 0 and c != 0:
        b == sqrt(c**2 - a**2)
    elif c == 0 and a != 0 and b != 0:
        c == sqrt(a**2 + b**2)    

    return a, b, c

