
def loadSeq(fileName):
    file = open(fileName,"r")
    dna_seq = ""
    for line in file:
        dna_seq +=line
    return dna_seq
