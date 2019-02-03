class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        evensum = 0
        for a in A:
            if a % 2 == 0:
                evensum += a
        
        ans = []
        for query in queries:
            if A[query[1]] % 2 == 0 and query[0] % 2 == 0: # add to even
                evensum += query[0]
            elif A[query[1]] % 2 == 0 and query[0] % 2 != 0: # not even anymore
                evensum -= A[query[1]]
            elif A[query[1]] % 2 != 0 and query[0] % 2 != 0: # not even anymore
                evensum += A[query[1]] + query[0] # New even number
            A[query[1]] += query[0]
            
            ans.append(evensum)
        return ans
                
        