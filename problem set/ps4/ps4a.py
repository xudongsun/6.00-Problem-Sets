# Problem Set 4A
# Name: Xudong Sun
# Collaborators: Ben Ruijl (line47-56, rewrite from his code on StackOverflow)
# Time Spent: 4:00

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
    if len(sequence) == 1:
        return [sequence]
    else:
        
        '''
        Suppose there are n characters in given sequence,
        
        for every character, there are (n-1)! permutations for the string that 
        starts with this character. 
        
        Thus the total number of permutations is n*(n-1)!=n!

        to avoid the repeat characters we firstly deal with index        
        '''
        # get the lenth of given sequence
        n = len(sequence)
        # mutate the sequence into a string of index
        index = ''
        for i in range(n):
            index += str(i)
        
        # solve the permutations of this index string
        permutations_index = []
        for j in range(n):
            # use recursion: firstly get the permutations of n-1 indexes
            # other than what is chosen
            index_rest = index[:j] + index[j+1:]
            permutation_rest = get_permutations(index_rest)
            # then put the chosen index into a certain position
            # to form a permutation of n indexes
            for char in permutation_rest:
                permutations_index.append(index[j] + char)
        # apply this method to every index    
        
        # for an arbitrary string, we can firstly match the index with chatacter
        # then exclude the repeat ones
        permutations = []        
        for index_s in permutations_index:
            s = ''
            for i in index_s:
                s += sequence[int(i)]
                
            if s not in permutations:
                permutations.append(s)
        
        return permutations
            
                
        
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input1 = '1'
    print('Input:', example_input1)
    print('Expected Output:', ['1'])
    print('Actual Output:', get_permutations(example_input1))
    
    example_input2 = 'abca'
    print('Input:', example_input2)
    print('Expected Output:', ['abca', 'abac', 'acab', 'acba', 'aabc', 'aacb', 'baac', 'baca', 'bcaa', 'caab', 'caba', 'cbaa'])
    print('Actual Output:', get_permutations(example_input2))
    
    example_input3 = 'abc'
    print('Input:', example_input3)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input3))
