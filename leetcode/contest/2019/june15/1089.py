class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        shift = [0 for i in range(0, len(arr))]
        count = 0
        for i in range(0, len(arr)):
            shift[i] = count
            if arr[i] == 0:
                count += 1
        print(shift)
        for i in range(len(arr)-1, -1, -1):
            if i + shift[i] >= len(arr):
                continue
            else:
                arr[i+shift[i]] = arr[i]