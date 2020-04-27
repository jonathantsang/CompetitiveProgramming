class Solution:
    def reformat(self, s: str) -> str:
        chars = []
        nums = []
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                chars.append(c)
        if abs(len(chars) - len(nums)) >= 2:
            return ""
        i = 0
        ans = []
        for i in range(0, min(len(nums), len(chars))):
            if len(chars) >= len(nums):
                ans.append(chars[i])
                ans.append(nums[i])
            elif len(chars) < len(nums):
                ans.append(nums[i])
                ans.append(chars[i])
        # print(ans)
        if len(chars) > len(nums):
            ans.append(chars[-1])
        elif len(chars) < len(nums):
            ans.append(nums[-1])

        return "".join(ans)
