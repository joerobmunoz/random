#Consider an arbitrary string X = x_1...x_n.  
#A subsequence of X is a string of the form 
#x_i_1 x_i_2...x_i_k ,where 1 <= i_1< ... < i_k <= n.  
#A string is palindromic if it is equal to its 
#own reverse (i.e. the string is the same whether 
#read backwards or forwards).  

# Write a dynamic programming algorithm based on the recurrence for L(i, j) in python.  Use backtracking 
    # to construct a longest palindromic subsequence.

# What is its running time?
    # O(n^2)
    
def lps(s):
    """Returns a longest palindromic subsequence of the string s."""
    l = [[0 for c in s] for c in s]
    
    n = len(s)
    
    for i in range(len(s)):
        l[i][i] = 1 # Every single character string has best length of 1
        
    cl = 2 # exclude base case
    while (cl <= n):
        i = 0
        while (i < n-cl+1): # fill out table diagonally
            j = i+cl-1
            if s[i] == s[j]:
                # outer letters match
                l[i][j] = l[i+1][j-1] + 2
            else:
                # no match, assign smallest "cost"
                l[i][j] = max(l[i][j-1], l[i+1][j])
            i += 1
        cl += 1
    
    return backtrack(l,s)

def backtrack(l,s):
    pal = ''
    i = 0;
    j = len(s)-1;
    while (i < j):
        if s[i] == s[j]:
            pal += s[i]
            i += 1
            j -= 1
        elif l[i][j-1] > l[i+1][j]:
            j -= 1
        else:
            i += 1
            
    if i == j:     
        pal += s[i] + pal[::-1]
    else:
        pal += pal[::-1]
    
    return pal

def main():
    assert(lps('axayyybaxca4baza') in ['aabacabaa','axayyyaxa', 'aabaxabaa'])
                                        
if __name__ == "__main__":
    main()
