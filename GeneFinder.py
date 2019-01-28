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
NAME : codingStrandToAA
PARAMETERS : string representing dna nucleotide sequence 
FUNCTION : takes a dna sequence and generates the appropriate Amino acid Sequence  
RETURN :  String representing the corresponding amino acids 
TIME COMPLEXITY : theta(n) where n is the size of the dna_seq
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

    print(codon_list)
def main():
    dna_seq = "CCCATGTTTTGAAAAATGCCCGGGTAAA"
    dna_seq1 = "CCATGTAGAAATGCCC"
    dna_seq2 = "ATGCCCATGGGGAAATTTTGACCC"

    oneFrame(dna_seq)
    oneFrame(dna_seq1)
    oneFrame(dna_seq2)



main()