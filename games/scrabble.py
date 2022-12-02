# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:03:28 2017

@author: James Rocker
"""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}


def scrabble_score(word):
    lst = []
    word = word.lower()
    for letter in word:
        for key in score:
            if letter == key:
                lst.append(score[key])
            else:
                continue
    return sum(lst)


print(scrabble_score(input('what is the longest word you can think of? I will give you the scrabble points for it. ')))
