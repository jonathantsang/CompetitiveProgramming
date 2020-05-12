class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        amt = 0

        for i in range(len(arr)-1):
            asofar = arr[i]

            for j in range(i+1, len(arr)):
                bsofar = arr[j]

                # test same without changing it
                if asofar == bsofar:
                    amt += 1

                for k in range(j+1, len(arr)):
                    bsofar ^= arr[k] # as k increases j has more
                    if asofar == bsofar:
                        amt += 1

                asofar ^= arr[j] # as j increases i has more

        return amt
