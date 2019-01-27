
'''
NAME : reverseComplement
PARAMETERS : string representing dna sequence
FUNCTION : takes a dna sequence and generates its complement in 5' to 3' order
RETURN :  string representing dna sequence complement
TIME COMPLEXITY : theta(n) where n is the size of the dna_seq
'''
def reverseComplement (dna_seq):
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
FUNCTION : takes a dna sequence and generates 
RETURN :  string representing dna sequence complement
TIME COMPLEXITY : theta(n) where n is the size of the dna_seq
'''
def codingStrandToAA(DNA):


def main():
    dnaseq = "TTGAC"
    print(reverseComplement(dnaseq))
main()

