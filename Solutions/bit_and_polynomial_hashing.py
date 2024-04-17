"""
Main concepts used: polynomial hash, Fenwick tree (although this could also be implemented with a segment tree)

Polynomial hash explained:
- A polynomial hash is a method of string hashing that only uses multiplication and addition

- A general polynomial hash follows the pattern: (a*P^N-1 + b*P^N-2 + c*P^N-3...x*P^2 + y*P^1 + z*P^0) % M 
     -> (letters all represent some number, whether it be actual numbers or ASCII codes of letters)
     -> P is some prime base for the hash function
        -> **some unique mathematical things regarding P needs research for understanding 
        regarding the increase of the base for less hash collisions**
     -> M is some large prime to mod the end value by 
        -> M >>>>> P (M should be much bigger than P)
        
- There are many ways to generate a polynomial hash:
    -> One way is through the use of a sliding window to create a rolling hash:
        - from the above equation for a generic polynomial hash
          we can factor it to see that it also follows: z + P(y + P(x + P(...b + P(a))))
            -> from this the rolling hash can be broken down into a sequence of multiplications and additions
                -> more specifically this sequence:
                    hash *= P
                    hash += val (where val is the number value we want to add to our hash)
                    
    -> Another way is to use prefix sums/prefix hashes: 
        - say we want to generate a polynomial hash for the substring from index i to j
            -> hash needed: a_1 * P^j-1 + a_2 * P^j-2 + a_3*P^j-3 .., a_i*P^0
               hash of ind 1 to j: a_1 * P^j-1 + a_2 * P^j-2 + a_3*P^j-3 .., a_j*P^0
               hash of ind 1 to i - 1: a_1 * P^i-1 + a_2 * P^i-2 + a_3*P^i-3 .., a_i-1*P^0
               
               since i exists before j, we can substract the hash of i - 1 from j to obtain a hash for i to j
               Formula generalizes to: H(i,j) = (H[1, j]-H[1, i-1]*B^(j-i+1) ) % MOD
               
        - this method is more easily understood through an example:
            -> say we have the array [1, 2, 3] we want to hash
            
            goal: obtain hash for index 2 to 3
            
            target hash: 2*P^1 + 3*P^0
            prefix hash of 3: 1*P^2 + 2*P^1 + 3*P^0
            prefix hash of 2-1 (1): 1*P^0
            
            1*P^2 + 2*P^1 + 3*P^0 - (1*P^0 * P^3-2+1) = 1*P^2 + 2*P^1 + 3*P^0 - 1*P^2 = 2*P^1 + 3*P^0
            
            
        - Resources: https://codeforces.com/blog/entry/18407 / https://codeforces.com/blog/entry/60445
        
        
Main ideas of implementation explained:
- Each index i will hold a partial hash for elements from index i - LSB(i) to i
    -> for example:
        - index 4 (0100 in binary) will hold a partial hash for elements from index 0 to 4
        - index 10 (1010 in binary) will hold a partial hash for elements from index 8 (10 - 2) to 10 
        
    -> how do we construct our tree?
        - say we have array [1, 2, 3, 4]
        (| bars represent areas of responsibility, for more info: https://www.youtube.com/watch?v=BHPez138yX8)
        4         | 1*P^3 + 2*P^2 + 3*P^1 + 4*P^0
        3 011 |   | 3*P^0
        2 010   | | 1*P^1 + 2*P^0
        1 001 | | | 1*P^0
        
        How can we construct the above tree?
            -> generic fenwick construction adds the value of a current ind to the value at index ind + LSB(ind)
            -> we can follow the same construction:
                -> tree initially starts off as the unchanged array (though it would be 1 indexed)
                -> for each iteration in construction, we add fenwick[i] * P^LSB(i) to fenwick[i + LSB(i)]
        
        
- Using the partial hashes, we can generate a prefix hash for any index and use that prefix hash 
and the formula explained in the polynomial hash section to generate any hash we want
    -> How can we generate prefix hash from partial hash?
    
    yet again this is better explained through an example:
    
    4         | 1*P^3 + 2*P^2 + 3*P^1 + 4*P^0
    3 011 |   | 3*P^0
    2 010   | | 1*P^1 + 2*P^0
    1 001 | | | 1*P^0
    
    # TODO: fix this section
    - for each iteration in summing:
        -> generic fenwick prefix sums are achieved by adding all fenwick values of the desired index's active bits
        -> multiplier variable set to 0 at first
        -> add current current fenwick[i] * P^multiplier to total
        -> add LSB(i) to multiplier
    
    example using 3:
    target hash: 1 * P^2 + 2*P^1 + 3*P^0
    
    # TODO: fix this section
    summing using fenwick:
    -> add fenwick[3] * P^multiplier(0 currently) -> 1(3*P^0) = 3*P^0
    -> add LSB(3) to multiplier (1 after update)
    -> subtract LSB(3) from 3 -> turns to 2
    -> add fenwick[2] * P^multiplier(1 currently) -> P(1*P^1 + 2*P^0) = 1 * P^2 + 2*P^1
    -> total = 1 * P^2 + 2*P^1 + 3*P^0
"""

P = 209389283097
M = 10**9 + 7
class BIT_and_polynomial_hashing:
    def __init__(self, arr, N):
        self.arr = arr
        self.N = N
        self.fenwick = self.construct(arr)

    # Fenwick implementation
    # Function to get least significant bit (LSB)
    def LSB(self, x):
        return x & -x

    # Function to construct fenwick tree to maintain polynomial hash
    def construct(self, arr):
        fenwick = arr.copy()
        # fenwick = [0] * (self.N + 1)
        for i in range(1, len(fenwick)):
            # self.update(i, arr[i])
            # below is ~O(N) method of constructing fenwick tree
            j = i + self.LSB(i)
            if j < len(fenwick):
                fenwick[j] += (fenwick[i] * pow(P, self.LSB(i), M)) % M
                fenwick[j] %= M
        return fenwick

    # Function to get prefix sums from fenwick tree
    def prefix_sum(self, pos):
        tot = 0
        # iteration = 0
        init_pos = pos
        while pos > 0:
            tot += (self.fenwick[pos] * pow(P, init_pos - pos, M)) % M  # might need mod after
            tot %= M
            # iteration += LSB(pos)
            pos -= self.LSB(pos)
        return tot

    # Function to get range sums from fenwick tree using prefix sums
    def query(self, l, r):
        return (self.prefix_sum(r) - self.prefix_sum(l - 1) * pow(P, r - l + 1, M)) % M

    # Function to update values in the fenwick tree
    def update(self, pos, diff):
        init_pos = pos
        while pos < len(self.fenwick):
            self.fenwick[pos] += (diff * pow(P, pos - init_pos, M)) % M
            self.fenwick[pos] %= M
            # iteration += LSB(pos)
            pos += self.LSB(pos)
        return
