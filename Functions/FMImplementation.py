from Functions.FMIndex.fmindex import *
import math
class Implementation:
    def __init__(self, location): 
        self.fileloc = location
        with open(location) as file:
            data = file.read().replace('\n', '')
            self.fmindex = create_fm_index(data)
            self.n = len(data)
    def search(self, query):
        ''' 
        returns list of all occurences of query/substring/gene
        '''
        return self.fmindex.search(query)

    def correction(self, string1, string2, approxpos=None):
        ''' 
        args:
                string1,
                string2,
                approxpos
            returns:
                string raising error or accepting if string has been changed on the data.

        If there are no syntax and formatting errors then it searches for string1 in the data
        If found, it replaces string1 with string2 and overwrites the file
        If there are multiple occurrences and approximate position is given by user
        then it replaces string that is closest to position. 
        '''
        for letter in string2:
            if letter not in 'ATGCatgc':
                return 'Your replacement seems to be invalid! You can only replace the gene with another gene (so input DNA letters)'
        if string2.isupper() == False:
            return 'Your replacement DNA is not in uppercase!'
        # Searching for string1 in the file
        Rs1 = self.fmindex.search(string1)
        originalf = open(self.fileloc, "r")
        lines = originalf.read()
        lines = str(lines)
        # If no instance found return no instance found.
        if len(Rs1)==0:
            return "No instance of Gene specified found"
        
        # if no approximate position is specified.
        # check if there aren't multiple results. If a single result is obtained then replace
        # else return error.
        if approxpos==None:
            if len(Rs1)==1:
                lines = lines[:Rs1[-1]] + str(string2) + lines[Rs1[-1]+len(string1):]
                originalf = open(self.fileloc, "w")
                originalf.writelines(lines)
                originalf.close()
                return string1 + " Now changed to " + string2
            else:
                return "Multiple Genes found, please specify what gene to change or pass in additional approximate positional argument"
        else:
        # if an approximate position is defined use that to find the best possible string near
        # the approx position. Replace the string at that position
            d = math.inf
            pos = -1
            positions = []
            # Finding the best possible postition near approximate position
            for i in Rs1:
                if abs(approxpos - i) < d:
                    d = abs(approxpos - i)
            # appending best possible position onto a list.
            for i in Rs1:
                if abs(approxpos - i) == d:
                    positions.append(i)
            # Might be a possibility that multiple positions are found so rasie an error.
            if len(positions)>1:
                return "Multiple instances found please specify better approximate position."
            print(positions)
            # Change the string accordingly
            lines = lines[:positions[-1]] + str(string2) + lines[positions[-1]+len(string1):]
            originalf = open(self.fileloc, "w")
            originalf.writelines(lines)
            originalf.close()
            return string1 + " Now changed to " + string2 + " at position " + str(positions[-1])

    def gene_analysis(self, string1, string2, approxlength=None):
        """
            args:
                string1,
                string2,
                approxlength
            
            return:
                Gene to be analyzed, if found.

        The function searches for the two strings, string1 and string2, and returns the approximate gene to be analized.
        Searching for the strings might result in multiple results fo the same gene. That is where the approxlength argument
        handles the error generated. It returns the Gene the most closely resembles the Gene with the approximate gene
        length specified. Why approximate? A biologist my want to consider the possibility of a mutation in the gene which
        he might want to change, hence the approximation.
        """
        if string2.isupper() == False or string1.isupper() == False:
            return 'Your DNA letters are not in uppercase!'
        for letter in string2:
            if letter not in 'ATGC':
                return 'Your input seems to be invalid! Please make sure that you have input DNA letters'

        # Searching for the strings
        Rs1 = self.fmindex.search(string1)
        Rs2 = self.fmindex.search(string2)

        # Checking arguments
        if approxlength!=None:
            d = math.inf
            lst = []
            for i in range(len(Rs1)):
                for j in range(len(Rs2)):
                    if Rs1[i] < Rs2[j] and abs(Rs2[j]-Rs1[i]-len(string1)-approxlength) < d:
                        d = abs(Rs2[j]-len(string1) -approxlength - Rs1[i])

            # Appending the indexes for approximate length onto a list
            for i in range(len(Rs1)):
                for j in range(len(Rs2)):
                    if abs(Rs1[i] < Rs2[j] and Rs2[j]-Rs1[i]-len(string1)-approxlength) == d:
                        lst.append((Rs1[i]+len(string1), Rs2[j]))

            # Handling returns if multiple instance found.
            if len(lst)>1:
                return "Multiple instances found please specify gene more correctly"
            else:
                if lst==[]:
                    return "No instance found"
                else:
                    file = open(self.fileloc, "r")
                    s = file.read()
                    file.close()
                    return s[ lst[-1][0] : lst[-1][1] ]

        # There might be a case where the genes to be specified are searched well enough that
        # there might be no requirement for approxlength. Thus this functionality.
        else:
            if len(Rs1) > 1 or len(Rs2) > 1:
                return "Multiple instances found please specify gene more correctly"
            elif Rs1==[] or Rs2==[]:
                return "No instance found"
            else:
                file = open(self.fileloc, "r")
                s = file.read()
                file.close()
                return s[ Rs1[-1]+len(string1) : Rs2[-1] ]
