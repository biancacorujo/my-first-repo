# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:17:12 2020

@author: Biancaca
"""

#Create a function that returns true if a number is even

def is_even (i):
    
    while i % 2 == 0:
        return True
    if i % 2 !=0:
        return False
    
    
print (is_even(2))


# Creare a function that returns false if a number is odd

def is_odd (i):
    while i % 2 != 0:
        return True
    if i % 2 == 0:
        return False
        
print (is_odd(3))

        
        
    