"""This module contains a function to translate RNA strands into proteins."""

# Mapping from proteins to their corresponding codons
P2C = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine': ['UUA', 'UUG'],
    'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine': ['UAU', 'UAC'],
    'Cysteine': ['UGU', 'UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA', 'UAG', 'UGA'],
}

# Invert the P2C mapping to create C2P
C2P = {c: p for p in P2C for c in P2C[p]}

def proteins(strand: str) -> list[str]:
    """Translate an RNA strand into a list of proteins.
    
    :param strand: The RNA strand to translate
    :type strand: str
    :returns: A list of proteins encoded by the RNA strand
    :rtype: list[str]
    """
    results = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        protein = C2P.get(codon)
        if protein == "STOP":
            break
        results.append(protein)
    return results
