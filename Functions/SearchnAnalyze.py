from Functions.FMImplementation import *
from Functions.FMIndex.fmindex import *
from Functions.RabinKarp.rabinkarp import *
from Functions.SuffixTree.suffixtree import *
from matplotlib import pyplot as plt
import numpy as np
import time, math, sys

# def search(txt, query):
#     res = [i for i in range(len(txt)) if txt.startswith(query, i)]
#     return res
def linear_substring_search(string, substring):
    '''
    Finds each occurence of the substring in the string and then returns the indexes for each
    '''
    indexes = []
    for i in range(len(string)):
        if string[i] == substring[0]: # if the current element is the same as the first element of the substring 
            if string[i:i+len(substring)] == substring: # then check the rest of the string. if it matches add the index of first letter to tthe list
                indexes.append(i)
    return indexes

########################################################################################################################################################################################################
def linear_find(filename, substring, time_bool=False):
    '''
    Reads a file and does linearSubStringSearch on it
    Either time taken for this substring search is returned or the list of indexes
    This depends on third argument
    '''
    for letter in substring:
        if letter not in 'ATGCatgc':
            return 'DNA pattern you are searching seems to be invalid! Input DNA letters'
    if substring.isupper() == False:
            return 'The DNA pattern you are searching is not in uppercase!'
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        start_time = time.time()
        result =  linear_substring_search(data, substring)
        print(result)
        end_time = time.time()
        if time_bool == False:
            return result
        else: # if timebool argument is given then even return the time taken to search 
            return (end_time - start_time)

def suffix_tree_find(filename, substring, time_bool=False):
    ''' 
    Reads a file and builds a suffix tree for it. Then the substring search is done on the file
    Either time taken for this substring search is returned or the list of indexes
    This depends on third argument
    '''
    for letter in substring:
        if letter not in 'ATGCatgc':
            return 'DNA pattern you are searching seems to be invalid! Input DNA letters'
    if substring.isupper() == False:
            return 'The DNA pattern you are searching is not in uppercase!'
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        tree = suffix_tree(data) # building the suffix tree
        start_time = time.time()
        result = tree.find_all(substring) # searching for first index of all occurrences of substring
        print(result)
        end_time = time.time()
        if time_bool == False:
            return result
        else: # if timebool argument is given then even return the time taken to search
            return (end_time - start_time)

def rabin_karp_find(filename, substring, time_bool = False):
    ''' 
    Reads a file then the substring search is done using hashing on the file
    Either time taken for this substring search is returned or the list of indexes
    This depends on third argument
    '''
    for letter in substring:
        if letter not in 'ATGCatgc':
            return 'DNA pattern you are searching seems to be invalid! Input DNA letters'
    if substring.isupper() == False:
            return 'The DNA pattern you are searching is not in uppercase!'
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        start_time = time.time()
        x = rabin_karp(substring, data)
        end_time = time.time()
        if time_bool == False:
            return x
        else:
            return (end_time-start_time)

def fm_index_find(filename, substring, time_bool=False):
    ''' 
    Reads a file and builds a FM-Index for it. Then the substring search is done on the file
    Either time taken for this substring search is returned or the list of indexes
    This depends on third argument
    '''
    for letter in substring:
        if letter not in 'ATGCatgc':
            return 'DNA pattern you are searching seems to be invalid! Input DNA letters'
    if substring.isupper() == False:
            return 'The DNA pattern you are searching is not in uppercase!'
    I = Implementation(filename) # creating an implementation object that builds an fm-index for a given file
    start_time = time.time()
    result = I.search(substring) # searching for first index of all occurrences of substring 
    print(result)
    end_time = time.time()
    if time_bool == False:
        return result
    else: # if timebool argument is given then even return the time taken to search
        return (end_time - start_time)

############################################################################################################################################################################
def plot(expected, title, n, color):
    ''' 
    Plots a histogram for a list of expected values
    Resulting graph will give the most expected value at mean
    '''
    bins = 20 
    binWidth = (max(expected) - min(expected)) / bins 
    plt.hist(expected, bins=bins , weights=np.ones(len(expected))/(len(expected)*binWidth), color=color) # produce histogram 
    plt.xlabel("Expected Time when n="+str(n))
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show() 

def expected_linear_time(numExp, sample, filename, substring, title, color):
    ''' 
    Reads a file and does linear substring search on it multiple times
    Time taken for this substring search is stored each time to get a sample and then the mean/expected value is calculated
    This is repeated several times to get several expected values
    The Expected values are plotted using a histogram using helper function
    '''
    expected = np.zeros(numExp) # numpy array of all expected values
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        for i in range(numExp): # To find several expectations. numExp is the number of experiments
            timeTaken = [] 
            for j in range(sample): # To find expectation using several simulations of samples
                start_time = time.time()
                print( linear_substring_search(data, substring) )
                end_time = time.time()
                timeTaken.append(end_time-start_time)
                # print(i,j)
            expected[i] = sum(timeTaken)/sample
        plot(expected, title, len(data), color)

def expected_suffix_time(numExp, sample, filename, substring, title, color):
    ''' 
    Reads a file, builds its suffix tree and does a substring search on it multiple times
    Time taken for this substring search is stored each time to get a sample and then the mean/expected value is calculated
    This is repeated several times to get several expected values
    The Expected values are plotted using a histogram using helper function
    '''
    expected = np.zeros(numExp)  # numpy array of all expected values
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        tree = suffix_tree(data)
        for i in range(numExp): # To find several expectations. numExp is the number of experiments
            timeTaken = []
            for j in range(sample): # To find expectation using several simulations of samples
                start_time = time.time()
                print(tree.find_all(substring))
                end_time = time.time()
                timeTaken.append(end_time-start_time)
                # print(i,j)
            expected[i] = sum(timeTaken)/sample
        plot(expected, title, len(data), color)

def expected_rk_time(numExp, sample, filename, substring, title, color):
    ''' 
    Reads a file, does a substring search using hashing, on it multiple times
    Time taken for this substring search is stored each time to get a sample and then the mean/expected value is calculated
    This is repeated several times to get several expected values
    The Expected values are plotted using a histogram using helper function
    '''
    expected = np.zeros(numExp)  # numpy array of all expected values
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        for i in range(numExp): # To find several expectations. numExp is the number of experiments
            timeTaken = []
            for j in range(sample): # To find expectation using several simulations of samples
                start_time = time.time()
                x = rabin_karp(substring, data)
                end_time = time.time()
                timeTaken.append(end_time-start_time)
                # print(i,j)
            expected[i] = sum(timeTaken)/sample
    plot(expected, title, len(data), color)

def expected_fm_time(numExp, sample, filename, substring, title, color):
    ''' 
    Reads a file, builds its FM-Index and does a substring search on it multiple times
    Time taken for this substring search is stored each time to get a sample and then the mean/expected value is calculated
    This is repeated several times to get several expected values
    The Expected values are plotted using a histogram using helper function
    '''
    expected = np.zeros(numExp)  # numpy array of all expected values
    I = Implementation(filename) # creating an implementation object that builds an fm-index for a given file
    for i in range(numExp): # To find several expectations. numExp is the number of experiments
        timeTaken = []
        for j in range(sample): # To find expectation using several simulations of samples
            start_time = time.time()
            print( I.search(substring) )
            end_time = time.time()
            timeTaken.append(end_time-start_time)
            # print(i,j)
        expected[i] = sum(timeTaken)/sample
    plot(expected, title, I.n, color)

def line_plot(x_axis, fm_y, suffix_y, rk_y=False, line_y=False):
    '''
    Plots a line graph for the expected time taken for substring search using suffix and fm-index
    Linear search plot is optional
    '''
    if type(rk_y) == type(x_axis) and type(line_y) == type(x_axis):
        plt.plot(x_axis, line_y, label='Linear Search', color='orange')    
        plt.plot(x_axis, rk_y, label='Rabin Karp (hashing)', color='hotpink')
    plt.plot(x_axis, suffix_y, label='Suffix Tree', color='purple')
    plt.plot(x_axis, fm_y, label='FM-Index', color=None)
    plt.legend()
    plt.xlabel('log( Number of DNA letters )')
    plt.ylabel('log( Time (s) )')
    plt.title('Expected Time w.r.t file size (number of DNA letters)')
    plt.show()

#################################################################################################################################################################################################
def get_FM_build_time(filename):
    '''
    Returns the time taken to build the FM-Index for a given file with a certain number of letters of DNA
    '''
    start_time = time.time()
    I = Implementation(filename) # creating an implementation object that builds an fm-index for a given file
    end_time = time.time()
    return  (end_time-start_time)

def get_suffix_build_time(filename):
    '''
    Returns the time taken to build the Suffix Tree for a given file with a certain number of letters of DNA
    '''
    start_time = time.time()
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        tree = suffix_tree(data) # building suffix tree for the given data set
    end_time = time.time()
    return  (end_time-start_time)    

def build_time_analysis(x_axis, lst, n):
    '''
    Plots a line graph for the expected time taken for fm index and sufflix tree to be build based on size of data set
    '''
    expected_fm_build = []
    expected_suffix_build = []
    for name in lst: # for each file
        fm_build = []
        suffix_build = []
        for i in range(n): # getting expected build time for fm index and suffix tree, for each file
            fm_build.append(get_FM_build_time(name))
            suffix_build.append(get_suffix_build_time(name))
        # print(fm_build, suffix_build)
        expected_fm_build.append(sum(fm_build)/n)
        expected_suffix_build.append(sum(suffix_build)/n)
    plt.plot(x_axis, np.array(expected_suffix_build), label='Suffix Tree', color='purple')
    plt.plot(x_axis, np.array(expected_fm_build), label='FM-Index', color=None)
    plt.legend()
    plt.xlabel('Number of DNA letters (in millions)')
    plt.ylabel('Time (s)')
    plt.title('Expected build Time w.r.t file size (number of DNA letters)')
    plt.show()