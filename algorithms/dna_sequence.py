# Top-down algorithm design practice

""" A DNA sequence is a string made up of the letters A, T, G, and C. To find
the complement of a DNA sequence, A's are replaced by T's, T's by A's, G's
by C's, and C's by G's. For example, the complement of AATTGCCGT is
TTAACGGCA.

a. Write an outline in English of the algorithm you would use to find the
complement.
    1. Map all sequence letters to their corresponding complement
    2. Save them in a data structure
    3. Interpet input sequence
    4. Return corresponding input complements

b. Review your algorithm. Will any characters be changed to their complement
and then changed back to their original value? If so, rewrite
your outline. Hint: Convert one character at a time, rather than all of
the A's, T's, G's, or C's at once.
    No.

c. Using the algorithm that you have developed, write a function named
complement that takes a DNA sequence (a str) and returns the complement
of it.
"""

def complement(sequence):
    """ (str) -> str
    Return the complement of a DNA sequence.

    >>> sequence = [AATTGCCGT]
    'TTAACGGCA'
    """
