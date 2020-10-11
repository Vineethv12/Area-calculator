#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Which shape would you like to calculate the area for? Please enter the option number-")

print("1. Square\n2. Triangle\n3. Cylinder\n4. Cricle\n")

userChoice = int(input())

# square
if userChoice == 1:
    squareA = int(input("Please enter the length of side:"))
    squareCalculate = squareA * squareA
    squareCalculate = str(squareCalculate)
    print("The area of square is: " + squareCalculate)

# triangle
if userChoice == 2:
    triBase = int(input("Please enter length of base:"))
    triHeight = int(input("Please enter length of height:"))
    triCalculate = triBase * tri * 1/2
    triCalculate = str(triCalculate)
    print("The area of traingle is: " + triCalculate)
    
# cylinder
if userChoice == 3:
    cylR = int(input("Please enter the radius of the cylinder: "))
    cylH = int(input("Please enter the height of the cylinder: "))
    cylCalc = ((2*3.14) * (cylR*cylH)) + ((2*3.14) * (cylR*cylR))
    cylCalc = str(cylCalc)
    print("The area of cylinder is: " + cylCalc)

# circle
if userChoice == 4:
    circR = int(input("Please enter the radius of the circle: "))
    circCalc = 3.14 * (circR*circR)
    circCalc = str(circCalc)
    print("The area of circle is: " + circCalc)


# 
