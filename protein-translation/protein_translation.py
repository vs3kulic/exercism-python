"""This module contains a function to translate RNA strands into proteins."""

CODON_MAPPING = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

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
        protein = CODON_MAPPING.get(codon)
        if protein == "STOP":
            break
        results.append(protein)
    return results
