# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:34:02 2020

@author: Tejaswini...!
"""


#to check whether two numbers are equal or not
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
if ( a == b):
    print("a is equal to b")
else:
    print("a is not equal to b")

#addition of two numbers
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
add=a+b
print("addition of two numbers is:",add)
 
#finding square root of number
import math
a=int(input("enter the value of a:"))
b=math.sqrt(a)
print("square is",b)

#finding area of triangle
import math
print("area of triangle with sides")
a=int(input("enter length of first side a:"))    
b=int(input("enter the value of second side b:"))
c=int(input("enter the value of third side c:"))
p=(a+b+c)/2    #half of the perimeter
x=p-a
y=p-b
z=p-c
t=p*x*y*z
area=math.sqrt(t)
print("area of triangle is",area)

#solving a quadratic equation
from math import sqrt
print("Quadratic function : (a * x^2) + b*x + c") 
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
r=b**2 - 4*a*c
if r > 0:
   num_roots = 2
   x1 = (((-b)+sqrt(r))/(2*a))
   x2 = (((-b)-sqrt(r))/(2*a))
   print("There are 2 roots:%f and %f"%(x1,x2))
elif r == 0:
   num_roots = 1 
   x=(-b)/2*a
   print("there is one root:", x)
else:
    num_roots = 0
    print("no roots,discriminant < 0.")
    exit()        