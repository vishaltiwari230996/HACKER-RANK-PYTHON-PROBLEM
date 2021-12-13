# -*- coding: utf-8 -*-
"""
AUTHOR :- Vishal Tiwari

This file contains alls the solution along with the questions link you need to go from 0 to 1 star on hacker rank 
"""
'''question 1 : 
    link :- https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
'''

'''if __name__ == '__main__': // uncomment to run this code 
    a = int(input())
    b = int(input())
    print(a//b)       // this is for the integer division means it will return the integral value of the divison
    print(a/b)       // this is for the float division 
'''   




''' question 2 :
      link :- https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
'''
"""  
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(i*i)
        
""" 



'''question 3 :
    link:-https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
'''
"""
def is_leap(year):
    leap = False
    if(year%10!=0):
        if(year%4==0):
            leap=True
    if(year%4==0 and year%100==0 and year%400==0):
        leap = True
    
    return leap

year = int(input())
"""



''' question 4 : 
    link:-https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
'''
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

"""