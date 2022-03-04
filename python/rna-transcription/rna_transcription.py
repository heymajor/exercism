def to_rna(dna_strand):
    dna_strand = dna_strand.replace("C", "#")
    dna_strand = dna_strand.replace("G", "C")
    dna_strand = dna_strand.replace("#", "G")
    dna_strand = dna_strand.replace("A", "#")
    dna_strand = dna_strand.replace("T", "A")
    dna_strand = dna_strand.replace("#", "U")
    return dna_strand

def main():
    print(to_rna("ACGTGGTCTTAA")) # UGCACCAGAAUU

if __name__ == '__main__':
    main()