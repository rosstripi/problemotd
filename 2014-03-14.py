"""
description: program to find longest palindrome in a string
author: rossbot
"""

def reverse(s):
    return s[::-1]

def find_palindrome(text):
    longest = ""
    for leng in range(2,len(text)+1):
        for pos in range(len(text)-leng+1):
            piece = text[pos:pos+leng]
            half = leng/2
            if piece[:half] == reverse(piece)[:half]:
                longest = piece
                break
    return longest
        
