"""
A module for RNA transcription.
"""

def to_rna(dna_strand):
    """
    Function to transcribe DNA to RNA. 

    param dna_strand: str
    return: str
    """
    mapping = {"G": "C", "C": "G", "T": "A", "A": "U"} # dna (key) to rna (value) mapping
    rna_strand = "".join([mapping[nucleotide] for nucleotide in dna_strand])

    return rna_strand
