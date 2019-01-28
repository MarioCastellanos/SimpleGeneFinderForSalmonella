"""
@AUTHOR : MARIO CASTELLANOS
@VERSION : 01.00.02
@DATE : 01/26/19

DESCRIPTION :  The function in this file is intended to open a file skip the first line
               then reading and storing the following dna sequence
    FUNCTIONS: loadSeq(fileName)

"""


"""
NAME : loadSeq
PARAMETERS : @param fileName: a string that represents the name of the file containing the DNA sequence 
FUNCTION : opens a the file passed as a parameter and extracts the dna sequence
RETURN :  string representing dna sequence 
TIME COMPLEXITY : theta(n) where n is the size of the dna_seq
"""


def loadSeq(fileName):
    file = open(fileName,"r")
    file.readline()
    dna_seq = ""
    for line in file:
        dna_seq +=line
    file.close()
    return dna_seq
