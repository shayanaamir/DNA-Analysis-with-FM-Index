# CS 201 Data Structures II Project, Spring 2021 
# Team: Amortized Properties

## Aim
To implement all our learnings of the studied data structures and even research and implement another one: FM-Index 
This is being done by making an application for a Bio-Informatics Scientist who can search, analyse, and alter genomic data.

## Overview
Main programming language used is python. This project imports several preinstalled packages but even numpy, matplotlib and PyQt libraries which you should install before attempting to run this application. 
If you do not have these packages, you can install them by going to the Resouces folder and then opening command prompt(type cmd on the navigation bar or however you want to open command prompt with the directory of the resources folder) simply running the following in command prompt:  
pip install -r requirements.txt   
For the GUI the PyQt library is mainly being used.    
The application implements FM-Index for all the different features and uses. For comparison of efficieny of FM-Index with other data structures that were studied, Suffix Tree, Rabin Karp (using hashing), and Linear search have also been implemented.

## Running the Application
Just run the MainWindow.py to start the application

## Back End Testing
Along with testing the application you can also test the algorithms separately, in the back end, in Testing.py 

## Data Sets
All DNA Data Sets for testing purposes have been taken from http://www.faculty.ucr.edu/~mmaduro/random.htm 
  
## Resources and References 
* https://www.geeksforgeeks.org/pattern-searching-using-suffix-tree/
* https://www.geeksforgeeks.org/burrows-wheeler-data-transform-algorithm/
* https://www.geeksforgeeks.org/suffix-array-set-1-introduction/
* https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
* https://academic.oup.com/bioinformatics/article/34/3/416/4160683 
* https://www.labri.fr/perso/ruricaru/bioinfo_master2/cours3.pdf   
* https://users.dcc.uchile.cl/~gnavarro/ps/psc05.3.pdf
* https://www.youtube.com/watch?v=kvVGj5V65io 
* http://www.cs.jhu.edu/~langmea/resources/lecture_notes/10_bwt_and_fm_index_v2.pdf
* https://github.com/ptrus/suffix-trees 
* https://github.com/mccricardo/Rabin-Karp 

