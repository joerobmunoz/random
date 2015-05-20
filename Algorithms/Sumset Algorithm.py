# Given two sets A and B of integers, their sum set C is defined to be 
# C = {a+b: aA, bB}.  For each c \in C, let m(c)denote the number of ways in
# which c can be obtained, i.e., m(c) = |{(a,b) : a A, b B, a+c = c}|.
# For example, if A = {1,2,3} and B={0,1,4}, then their sum set is 
# C = {1,2,5,3,6,4,7} and 
# m(1) = 1, m(2) = 2, m(3) = 2, m(4) = 1, m(5)=1, m(6) = 1, and m(7) = 1. 

def sumset(n,A,B):
    # O(n log n) time.
    C = np.zeros(2*n,dtype= int)
    
    AA = np.zeros(2*n,dtype= int)
    BB = np.zeros(2*n,dtype= int)
    
    maxSum = max(A) + max(B)
    
    for a in A:
        AA[a] = 1
    for b in B:
        BB[b] = 1
    
    # Each index corresponds to a possible sum set
    c = np.convolve(AA,BB)
    
    # strip all non-possible indices. Leave the beginning index, because
    # it is stripped in list comprehension
    C = c[:maxSum+1]
    
    return [ (i,C[i]) for i in range(len(C)) if C[i] > 0]

def main():
    A = [1,2,3]
    B = [0,1,4]

    C = sumset(5,A,B)

    C.sort()

    assert (C == [(1, 1), (2, 2), (3, 2), (4, 1), (5, 1), (6, 1), (7, 1)])

if __name__ == "__main__":
    main()

