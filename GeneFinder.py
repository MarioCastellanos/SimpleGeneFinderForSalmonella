from dna import *
from Load import *

"""
@AUTHOR : MARIO CASTELLANOS
@VERSION : 01.00.04
@DATE : 01/31/19

DESCRIPTION : The purpose of this file is to be useed as the driver for Load.py and dna.py
    FUNCTIONS: oneFrame(DNA) 
"""


'''
NAME : oneFrame
PARAMETERS : @param DNA: a string representing a DNA sequence
FUNCTION : starts at the 0 position of DNA and searches forward 
           in units of three looking for start codons. When it 
           finds a start codon, oneFrame takes the slice of 
           DNA beginning with that "ATG" for the open reading frame
           that begins there until the stopping codon (TAG, TGA, or TAA). 
           Adding the open reading frame to a list of reading frames ORFL. 
           If there is no in frame stopping codon then it assumes that the 
           reading frame extends beyond the given DNA sequence and simply 
           adds the entire sequence from "ATG" to the end to the reading 
           frames list. 
RETURN :  the list of all ORFs found 
'''

def oneFrame(DNA):
    codon_list = []
    for i in range(0, len(DNA), +3):
        curr_codon = DNA[i:i+3]
        if curr_codon == "ATG":
            Finished = False
            loc = i
            CCF = curr_codon # CCF is short for Current Codon in Frame  and stores the current codon for the ORF
            curr_Frame = ""
            while loc < len(DNA) and not Finished:
                CCF = DNA[loc:loc+3]
                if CCF != "TAG" and CCF != "TGA" and CCF != "TAA":
                    curr_Frame += CCF
                else :
                    Finished = True
                loc += 3
            codon_list.append(curr_Frame)

    return codon_list


"""
NAME: oneFrameV2
PARAMETERS : @param DNA :a string representing a DNA sequence
FUCNTION : starts at the 0 position of DNA and searches forward 
           in units of three looking for start codons. When it 
           finds a start codon, oneFrame takes the slice of 
           DNA beginning with that "ATG" for the open reading frame
           that begins there until the stopping codon (TAG, TGA, or TAA). 
           Adding the open reading frame to a list of reading frames ORFL. 
           If there is no in frame stopping codon then it assumes that the 
           reading frame extends beyond the given DNA sequence and simply 
           adds the entire sequence from "ATG" to the end to the reading 
           frames list. If any nested frames are found only the larger reading
           frame is added to the list. 
OUTPUT :  the list of all ORFs found that are not nested 
comment : I believe that there is a faster way to implement without calling 
           calling one frame by processing the DNA and not adding the nested
           reading frames instead of processing the list of reading frames 
           with nested frames. I believe it to be faster as the  DNA 
           sequence would only be processed once without the additional burden 
           of list manipulation. 
"""


def oneFrameV2(DNA):
    ORFL = oneFrame(DNA)  # Open reading frame list
    for index in range(0,len(ORFL),3):
        curr_Frame = ORFL[index][3:]
        for i in range(0,len(curr_Frame),3):
            if curr_Frame[i:i+3] == "ATG":
                ORFL.pop(index+1)
    return ORFL

def longestORF(DNA):
    for i in range(0,3,1):
        print(DNA[i:])



def main():

    dna_seq = "CCCATGTTTTGAAAAATGCCCGGGTAAA"
    dna_seq1 = "CCATGTAGAAATGCCC"
    dna_seq2 = "ATGCCCATGGGGAAATTTTGACCC"
    dna_seq3 = "ATGCCCATGGGGAAATTTTGACCC" #print("ONEV2: ", oneFrameV2("ATGCCCATGGGGAAATTTTGACCC"))
    dna_seq4 = "ATGATGTAGAAAATGAAAAAATTT" #print("ONEV22: ", oneFrameV2("ATGATGTAGAAAATGAAAAAATTT"))







main()