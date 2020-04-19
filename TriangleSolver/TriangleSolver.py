"""
-------------------------------------------------------
This function uses the different formulas to solve a 
triangle in the most efficient way possible.
(SINE LAW, COSINE, LAW, PYTHAGOREAN THEOREM, ETC...)
------------------------------------------------------
"""
import equations   

def startMenu():
        print("""===========================================================================================
    Must provide at least 3 values, one of which must be a side length.
    If a right triangle, must be given at least 2 values.
    Upper case values (A, B, C) are angles, while lower case(a, b, c) are for side lengths.
    ===========================================================================================""")
        print("\nType of Triangle:")
        print("(1) Right Triangle \n(2) SSS \n(3) SAS \n(4) ASA")
        triangleTypeInput = int(input("Enter Type of Triangle: "))
        a, b, c, A, B, C = triangleType(triangleTypeInput)
        triangleSolved(a, b, c, A, B, C)
        print("Completed")


def triangleValues(triangleTypeInput):
    if triangleTypeInput == 1:
        print("\nKeep unknown values blank")
        a = float(input("a : ") or int(0))
        b = float(input("b : ") or int(0))
        c = float(input("Hypoteneuse : ") or int(0))
        A = int(45)
        B = int(45)
        C = int(90)
    else:
        print("\nKeep unknown values blank")
        a = float(input("a : ") or int(0))
        b = float(input("b : ") or int(0))
        c = float(input("c : ") or int(0))
        A = float((input("A(Degrees) : ") or int(0)))
        B = float((input("B(Degrees) : ") or int(0)))
        C = float((input("C(Degrees) : ") or int(0)))

    return a, b, c, A, B, C

def triangleType(triangleTypeInput):
    a, b, c, A, B, C = triangleValues(triangleTypeInput)
    if triangleTypeInput == 1:
        a, b, c = equations.rightTriangle(a, b, c)
    elif triangleTypeInput == 2:
        A, B, C = equations.sss(a, b, c)
    elif triangleTypeInput == 3:
        a, b, c, A, B, C = equations.oneAngle_twoSide(a, b, c, A, B, C)
    elif triangleTypeInput == 4: 
        a, b, c, A, B, C = equations.twoAngle_oneSide(a, b, c, A, B, C)
    else:
        print("Cannot solve Triangle.")

    return a, b, c, A, B, C

def triangleSolved(a, b, c, A, B, C):
    print ("\n\nTriangle")
    print ("a : {:.2f}".format(a))
    print ("b : {:.2f}".format(b))
    print ("c : {:.2f}".format(c))
    print ("A : {:.2f} Degrees".format(A))
    print ("B : {:.2f} Degrees".format(B))
    print ("C : {:.2f} Degrees".format(C))

    return 

startMenu()

