class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        leng = len(nums)
        output = []
        for i in range(0,leng):
            output.append(p)
            p = p * nums[i]
        p = 1
        print(output)
        for i in range(leng-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
        