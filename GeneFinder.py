from dna import *
from Load import *

"""
@AUTHOR : MARIO CASTELLANOS
@VERSION : 01.00.02
@DATE : 01/28/19

DESCRIPTION : The purpose of this file is to be useed as the driver for Load.py and dna.py
    FUNCTIONS: oneFrame(DNA) 
"""


'''
NAME : oneFrame
PARAMETERS : @param DNA: a string representing a DNA sequence
FUNCTION : starts at the 0 position of DNA and searches forward 
           in units of three looking for start codons. When it 
           finds a start codon, oneFrame should take the slice of 
           DNA beginning with that "ATG" for the open reading frame
           that begins there until the stopping codon (TAG, TGA, or TAA). 
           Adding the open reading frame to a list of reading frames. 
           If there is no in frame stopping codon then it assumes that the 
           reading frame extends beyond the given DNA sequence and simply 
           adds the entire sequence from "ATG" to the end to the reading 
           frames list. 
RETURN :  the list of all ORFs found 
TIME COMPLEXITY : 
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
FUCNTION : parses through the possible ORF in A
OUTPUT : 
TIME_COMPLEXITY : 
"""
def oneFrameV2(DNA):
    ORFL = oneFrame(DNA)  # Open reading frame list
    #print(ORFL)
    for index in range(0,len(ORFL),3):
        curr_Frame = ORFL[index][3:]
        for i in range(0,len(curr_Frame),3):
            #print("curr_frame: ", curr_Frame[i:i + 3])
            if curr_Frame[i:i+3] == "ATG":
                print("curr_frame: ", curr_Frame[i:i+3])
                print("len: ",len(ORFL))
                print("index: ",index+1,)
                ORFL.pop(index+1)
    return ORFL


def main():

    dna_seq = "CCCATGTTTTGAAAAATGCCCGGGTAAA"
    dna_seq1 = "CCATGTAGAAATGCCC"
    dna_seq2 = "ATGCCCATGGGGAAATTTTGACCC"

    ###neFrame(dna_seq2)

    print(oneFrameV2("ATGCCCATGGGGAAATTTTGACCC"))
    print(oneFrameV2("ATGATGTTTAAAATGAAAAAATTT"))



main()