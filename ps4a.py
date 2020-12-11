# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
from itertools import permutations

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    from itertools import permutations 

    out = []
    if len(sequence) == 1:
        return sequence
    else:
        for i,let in enumerate(sequence):
            for perm in get_permutations(sequence[:i] + sequence[i+1:]):
                out += [let + perm]
    return out


if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))


