from Functions.SearchnAnalyze import *

######################################## Testing for 1 search #########################################################################################################
print(get_FM_build_time('DataSets/100000.txt'))
print(get_suffix_build_time('DataSets/100000.txt'))

# linear_find('DataSets/10000.txt', 'AAT')
# suffix_tree_find('DataSets/10000.txt', 'AAT')
# fm_index_find('DataSets/10000.txt', 'AAT')
# rabin_karp_find('DataSets/10000.txt', 'AAT')

# print('Linear Search Time', linear_find('DataSets/10000.txt', 'AAT', True))
# print('Suffix Tree Search Time', suffix_tree_find('DataSets/10000.txt', 'AAT', True))
# print('FM Index Search Time', fm_index_find('DataSets/10000.txt', 'AAT', True))
# print('Rabin Karp Search Time', rabin_karp_find('DataSets/10000.txt', 'AAT', True))

################################### Testing for expected time ####################################################################################################
######################################## LINEAR SEARCH ##########################################
# expected_linear_time(250, 50, 'DataSets/1000.txt', 'GGAATT', 'Linear Search', 'orange')
# expected_linear_time(10, 50, 'DataSets/10000.txt', 'CTCGTGA', 'Linear Search', 'orange')
# expected_linear_time(250, 50, 'DataSets/100000.txt', 'TATGCAC', 'Linear Search', 'orange')
# expected_linear_time(250, 25, 'DataSets/1000000.txt', 'AGTACAGC', 'Linear Search', 'orange')
# expected_linear_time(250, 25, 'DataSets/2500000.txt', 'CACATTT', 'Linear Search', 'orange')

####################################### SUFFIX-TREE ############################################# 
# expected_suffix_time(250, 50, 'DataSets/1000.txt', 'GGAATT', 'Suffix-Tree', 'purple')
# expected_suffix_time(250, 50, 'DataSets/10000.txt', 'CTCGTGA', 'Suffix-Tree', 'purple')
# expected_suffix_time(250, 50, 'DataSets/100000.txt', 'TATGCAC', 'Suffix-Tree', 'purple')
# expected_suffix_time(250, 25, 'DataSets/1000000.txt', 'AGTACAGC', 'Suffix-Tree', 'purple')
# expected_suffix_time(250, 25, 'DataSets/2500000.txt', 'CACATTT', 'Suffix Tree', 'purple')

######################################### Rabin Karp (hashing) ##################################
# expected_rk_time(250, 50, 'DataSets/1000.txt', 'GGAATT', 'Rabin Karp (hashing)', 'hotpink')
# expected_rk_time(250, 50, 'DataSets/10000.txt', 'CTCGTGA', 'Rabin Karp (hashing)', 'hotpink')
# expected_rk_time(150, 25, 'DataSets/100000.txt', 'TATGCAC', 'Rabin Karp (hashing)', 'hotpink')
# expected_rk_time(20, 10, 'DataSets/1000000.txt', 'AGTACAGC', 'Rabin Karp (hashing)', 'hotpink')
# expected_rk_time(15, 10, 'DataSets/2500000.txt', 'CACATTT', 'Rabin Karp (hashing)', 'hotpink')

######################################## FM-INDEX ###############################################
# expected_fm_time(250, 50, 'DataSets/1000.txt', 'GGAATT', 'FM/-Index', None)
# expected_fm_time(250, 50, 'DataSets/10000.txt', 'CTCGTGA', 'FM-Index', None)
# expected_fm_time(250, 50, 'DataSets/100000.txt', 'TATGCAC', 'FM-Index', None)
# expected_fm_time(250, 25, 'DataSets/1000000.txt', 'AGTACAGC', 'FM-Index', None)
# expected_fm_time(250, 25, 'DataSets/2500000.txt', 'CACATTT', 'FM-Index', None)

############################################ Line Plot Analysis of time to Search ######################################################################################################
# x_axis = np.array([math.log(1000, 10), math.log(10000, 10), math.log(100000, 10), math.log(1000000, 10), math.log(2500000, 10)])
# line_y = np.array([math.log(0.0013, 10), math.log(0.0056, 10), math.log(0.040, 10), math.log(0.225, 10), math.log(0.6, 10)])
# suffix_y = np.array([math.log(0.00072, 10), math.log(0.0008, 10), math.log(0.00116, 10), math.log(0.00120, 10), math.log(0.0077, 10)])
# fm_y = np.array([math.log(0.0006, 10), math.log(0.00065, 10), math.log(0.0009, 10), math.log(0.0015, 10), math.log(0.0050, 10)])
# rk_y = np.array([math.log(0.0055, 10), math.log(0.049, 10), math.log(0.55, 10), math.log(5, 10), math.log(13, 10)])
# line_plot(x_axis,fm_y, suffix_y, rk_y, line_y)   
# line_plot(x_axis, fm_y, suffix_y)     

############################################ Line Plot Analysis of time to build #######################################################################################
# x = np.array([1000, 10000, 100000, 1000000, 2500000])
# file_lst = ['DataSets/1000.txt', 'DataSets/10000.txt', 'DataSets/100000.txt', 'DataSets/1000000.txt', 'DataSets/2500000.txt']
# build_time_analysis(x, file_lst, 5)

################################ Testing Gene Correction And Analysis #####################################################################################
# I = Implementation('DataSets/10000.txt')

# print(I.correction('TGCT', 'genomic data'))
# print(I.correction('TGCT', 'BIOINFORMATICS', 50))
# print(I.correction('TACG', 'ATGC', 50))

# print(I.gene_analysis('CCCC', 'Cmkwx'))
# print(I.gene_analysis('CCCC', 'CTMK'))
# print(I.gene_analysis('CCCC', 'AGTCA'))

# print(I.gene_analysis('CCCC', 'AGTCA', 100))