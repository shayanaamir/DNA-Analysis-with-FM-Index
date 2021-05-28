from collections import Counter
from Functions.FMIndex.sa import *
import argparse
import time
import os

# Using \0 for terminating character 
terminal_char = '\0'
def bw_transform(text, suffix_array):
    """ 
    Returns Buurows Wheeler Transform
    """
    bw = []
    for s in suffix_array:
        if s == 0: # if s is 0 then we have reached the end
            bw.append(terminal_char) 
        else:
            bw.append(text[s - 1])
    return ''.join(bw)  # return string version of list bw

def count_characters(text):
    """ 
    Returns a Counter object containing number of occurrences of each character in text 
    """
    return Counter(text)

def calculate_ranks(text):
    """ 
    Calculates rank of each character of input text 
    """
    count = Counter() # initialize counter object
    ranks = [] 
    for c in text:
        ranks.append(count[c])
        count[c] += 1
    return ranks

def terminate_string(s):
    """ 
    Terminates the string with terminal_char if it is not terminated already.
    This character needs to be the smallest character in entire string. 
    """
    return s if s[-1:] == terminal_char else s + terminal_char

class FColumn:
    def __init__(self, count, first_occurrence):
        self._count = count
        self._first_occurrence = first_occurrence

    def char_range(self, c):
        return (self.get_first_occurrence(c), self.get_first_occurrence(c) + self._count[c])

    def get_first_occurrence(self, c):
        return self._first_occurrence.get(c, 0)

class FMIndex:
    def __init__(self, bwt, sa, ranks, f_column):
        self._bwt = bwt # burrows wheeler transform
        self._sa = sa # suffix array
        self._ranks = ranks 
        self._f_column = f_column

    def _find_preceders(self, c, start, end):
        first_index = self._bwt.find(c, start, end)
        if first_index == -1:
            return (0, 0)
        else:
            return (self._ranks[first_index], self._bwt.count(c, first_index, end) )

    def search(self, pattern):
        if not pattern: # if false
            return []
        reverse_pattern = pattern[::-1] # string reversal
        start_index, end_index = self._f_column.char_range(reverse_pattern[0])
        for c in reverse_pattern[1:]:
            first_rank, count = self._find_preceders(c, start_index, end_index)
            if count == 0: # if no occurence then return empty list
                return []
            else:
                start_index = self._f_column.get_first_occurrence(c) + first_rank
                end_index = start_index + count 
        return sorted(self._sa[start_index:end_index]) 

def calculate_first_occurrences(counts):
    first_occurrences = {}
    s = 0
    for k, v in sorted(counts.items()):
        first_occurrences[k] = s 
        s += v
    return first_occurrences

def create_f_column(text):
    count = count_characters(text) # count of each character
    first_occurrence = calculate_first_occurrences(count)
    return FColumn(count, first_occurrence)

def create_fm_index(text):
    t = terminate_string(text) # terminates the string with terminal_char if it is not terminated already
    # sa = suffix_array_manber_myers(t)
    sa = suffix_array_best(t) # builds suffix array
    bwt = bw_transform(t, sa) # returns bwt using the string and suffix array
    ranks = calculate_ranks(bwt) # calculates rank for each character in bwt
    f_column = create_f_column(t)
    return FMIndex(bwt, sa, ranks, f_column)