"""
@AUTHOR : MARIO CASTELLANOS
@VERSION : 01.00.04
@DATE : 01/31/19

DESCRIPTION : The functions found in this file are used
              to manipulate DNA.
    FUNCTIONS: reverseComplement
               codingStrandToAA
"""



'''
NAME : reverseComplement
PARAMETERS : string representing dna sequence
FUNCTION : takes a dna sequence and generates its complement in 5' to 3' order
RETURN :  string representing dna sequence complement
TIME COMPLEXITY : theta(n) where n is the size of the dna_seq
'''


def reverseComplement(dna_seq):

    invese_len = (len(dna_seq)+1)*-1
    inverse_dna_seq_comp = ""
    curr_base = ""
    for i in range(-1,invese_len,-1):
        curr_base = dna_seq[i]
        if curr_base == "A" :
            curr_base = "T"
        elif curr_base == "T":
            curr_base  = "A"
        elif curr_base == "C":
            curr_base = "G"
        elif curr_base == "G":
            curr_base = "C"
        inverse_dna_seq_comp += curr_base
    return inverse_dna_seq_comp


'''
NAME : codingStrandToAA
PARAMETERS : string representing dna nucleotide sequence 
FUNCTION : takes a dna sequence and generates the appropriate Amino acid Sequence 
           using an arrangement of if else statements to determine the proper amino acid
           for each codon. 
RETURN :  String representing the corresponding amino acids 
TIME COMPLEXITY : theta(n) where n is the size of the dna_seq
'''


def codingStrandToAA(DNA):

    if len(DNA)% 3 == 0:
        AASEQ = ""
        for i in range (0,len(DNA),3):
            curr_codon = DNA[i:i+3]
            if curr_codon[0] == "T":
                if curr_codon[1] == "T":
                    if curr_codon[2] == "T" or curr_codon[2] == "C":
                        AASEQ += "F"
                    else :
                        AASEQ += "L"
                elif curr_codon [1] == "C":
                    AASEQ += "S"
                elif curr_codon[1] == "A" :
                    if curr_codon[2] == "T" or curr_codon[2] == "C":
                        AASEQ += "Y"
                    else:
                        AASEQ += ""
                else:
                    if curr_codon[2] == "T" or curr_codon[2] == "C":
                        AASEQ += "C"
                    elif curr_codon[2] == "A":
                        AASEQ += ""
                    else :
                        AASEQ +="W"
            elif curr_codon [0] == "C":
                if curr_codon[1] == "T":
                    AASEQ += "L"
                elif curr_codon[1] == "C":
                    AASEQ += "P"
                elif curr_codon[1] == "A":
                    if curr_codon[2] == "T" or curr_codon[2] == "C":
                        AASEQ += "H"
                    else:
                        AASEQ += "Q"
                else:
                    AASEQ += "R"
            elif curr_codon[0] == "A":
                if curr_codon[1] == "T" :
                    if curr_codon[2] == "T" or curr_codon[2] == "C"or curr_codon[2] == "A":
                        AASEQ += "I"
                    else:
                        AASEQ += "M"
                elif curr_codon[1] == "C":
                    AASEQ +="T"
                elif curr_codon[1] == "A":
                    if curr_codon[2] == "T" or curr_codon[2] == "C":
                        AASEQ += "N"
                    else:
                        AASEQ += "K"
                else :
                    if curr_codon[2] == "T" or curr_codon[2] == "C":
                        AASEQ += "S"
                    else:
                        AASEQ += "R"
            else:
                if curr_codon[1] == "T":
                    AASEQ += "V"
                elif curr_codon[1] == "C":
                    AASEQ += "A"
                elif curr_codon[1] == "A":
                    if curr_codon[2] == "T" or curr_codon[2] == "C":
                        AASEQ += "D"
                    else :
                        AASEQ += "E"
                else:
                    AASEQ += "G"
        return AASEQ
    else:
        print("DNA sequence not divisible by 3")
        return None