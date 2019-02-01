from dna import *
from Load import *
from random import*


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
"""


def oneFrameV2(DNA):
    ORFLNN = []  # Open Reading Frame List Non Nested Reading frames
    ENDLIST = []
    for i in range(0,len(DNA),3):
        curr_codon = DNA[i:i+3]
        if curr_codon == "ATG":
            curr_Frame = ""
            loc = i
            while loc< len(DNA) and curr_codon!= "TAG" and curr_codon != "TGA" and curr_codon != "TAA" :
                curr_Frame += DNA[loc:loc+3]
                curr_codon = DNA[loc:loc+3]
                loc+=3
            if loc not in ENDLIST:
                ORFLNN.append(curr_Frame)
                ENDLIST.append(loc)
    return ORFLNN

"""
NAME: longestORF
PARAMETERS: @param DNA :a string representing a DNA sequence
FUNCTION: function which calls oneFrameV2.to find the longest
          open reading frame of all 3 reading frames
OUTPUT: string representing the longest open reading frame
"""


def longestORF(DNA):
    max_len = 0
    max_frame = ""
    for i in range(0,3,1):
        curr_ORFL = oneFrameV2(DNA[i:])
        for frame in curr_ORFL :
            if len(frame) > max_len:
                max_frame = frame
    return max_frame


"""
NAME: longestORFBothStrands
PARAMETERS: @param DNA :a string representing a DNA sequence
FUNCTION: This function takes a DNA string as input and finds
          the longest ORF on that DNA string and its reverse
          complement.
OUTPUT: return a string representing the longest ORF of the 
        DNA string and its reverse complement
"""


def longestORFBothStrands(DNA):
    dna = longestORF(DNA)
    complement_dna = longestORF(reverseComplement(DNA))
    if len(dna) > len(complement_dna):
        return dna
    return complement_dna




"""
NAME: longestORFNoncoding 
PARAMETERS  :param DNA :a string representing a DNA sequence
            :param numReps is an integer that represents the amount of 
             garbage sequences to generate 
FUNCTION:  generates a bunch of garabage sequences used so we can cross reference 
           with our ORF to assess whether long ORFs are genes. 
OUTPUT:   returns an number reperesenting the lenght of the longest garbage ORF it found 
"""


def longestORFNoncoding(DNA, numReps):
    dna_seq_list = list(DNA)
    max_random = 0
    for i in range (0,numReps,1):
        shuffle(dna_seq_list)
        curr_random = longestORFBothStrands(collapse(dna_seq_list))
        if len(curr_random) > max_random:
            max_random = len(curr_random)
    return max_random



"""
NAME: collapse
PARAMETERS :parameter L a list of characters to join together 
FUNCTION: concatenates all characters in L to a single string 
OUTPUT: single string representing the concatenation of each element in L
"""


def collapse(L):
    str = ""
    for char in L:
        str+=char
    return str


"""
NAME: findORFs
PARAMETERS: :param DNA :a string representing a DNA sequence 
FUNCTION:   will identify all the ORFs in the real (un-shuffled) DNA 
OUTPUT:  returns a list of all the ORFs it identified if none were
         found an empty list is returned 
"""


def findORFs(DNA):
    ORFL = []
    for i in range(0,3,1):
        currFrame = DNA[i:]
        frame = oneFrameV2(currFrame)
        ORFL += frame
    return ORFL


"""
NAME: findORFsBothStrands
PARAMETERS: :param DNA :a string representing a DNA sequence 
FUNCTION:  searches both the forward and reverse complement strands for ORFs
OUTPUT: returns a list with all the ORFs found
"""


def findORFsBothStrands(DNA):
    ORFL = []
    inSeq = findORFs(DNA)
    complement = findORFs(reverseComplement(DNA))
    ORFl = inSeq + complement
    return ORFl


"""
NAME: 
PARAMETERS: 
FUNCTION: 
OUTPUT: 
"""


def getCoordinates(orf, DNA):
    coordinates = []
    #print(orf)
    index = DNA.find(orf)
    if index == -1:
        reverseOrf = reverseComplement(orf)
        index = DNA.find(reverseOrf)
    endcoordinate = index + len(orf)
    coordinates = [index, endcoordinate]
    return coordinates


"""
NAME: 
PARAMETERS: 
FUNCTION: 
OUTPUT: 
"""


def geneFinder(DNA, minLen):
    ORFL = findORFsBothStrands(DNA)
    ORFLM = []
    listofLists = []
    for orfl in ORFL:
        if len(orfl)>minLen:
            ORFLM.append(orfl)
    for frame in ORFLM:
        final = []
        #print("frame: ", frame)
        listL = getCoordinates(frame, DNA)
        pS = codingStrandToAA(frame)
        final = []
        for i in listL:
            final.append(i)
        final.append(pS)
        print(final)
        listofLists.append(final)

    listofLists.sort()
    return listofLists


"""
NAME: 
PARAMETERS: 
FUNCTION: 
OUTPUT: 
"""

def printGenes(geneList):
    for gene in geneList:
        print(gene)

def main():

    dna_seq = "CCCATGTTTTGAAAAATGCCCGGGTAAA"
    dna_seq1 = "CCATGTAGAAATGCCC"
    dna_seq2 = "ATGCCCATGGGGAAATTTTGACCC"
    dna_seq3 = "ATGCCCATGGGGAAATTTTGACCC" #print("ONEV2: ", oneFrameV2("ATGCCCATGGGGAAATTTTGACCC"))
    dna_seq4 = "ATGATGTAGAAAATGAAAAAATTT" #print("ONEV22: ", oneFrameV2("ATGATGTAGAAAATGAAAAAATTT"))
    dna_seq5 = "ATGAAATAG"
    dna_seq6 = "CATGAATAGGCCCA"
    dna_seq7 = "ATGCCCTAACATGAAAATGACTTAGG"
    dna_seq8 = "CTATTTCATG"
    dna_seq9 = "ATGGGATGAATTAACCATGCCCTAA"
    dna_seq10 = "GGAGTAAGGGGG"
    dna_seq11 = "ATGAAACAT" #findORFsBothStrands(dna_seq11)
    dna_seq12 = "ACGTTCGA" #getCoordinates("GTT",dna_seq12)
    dna_seq13 = "ACGTTCGA"#getCoordinates("CGAA",dna_seq13)

    X73525 = loadSeq("X73525.fa")
    min_val = longestORFNoncoding(X73525, 1500)
    geneList = geneFinder(X73525, min_val)
    printGenes(geneList)

main()