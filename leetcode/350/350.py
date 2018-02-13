class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shorter = 0
        if(len(nums1) < len(nums2)):
            shorter = 1
        else:
            shorter = 2
        inter = []
        ht= dict();
        if(shorter == 1):
            for i in range(0, len(nums2)):
                if nums2[i] not in ht:
                    ht[nums2[i]] = 1
                else:
                    ht[nums2[i]] = ht[nums2[i]] + 1
            for i in range(0, len(nums1)):
                if nums1[i] in ht and ht[nums1[i]] > 0:
                    inter.append(nums1[i])
                    ht[nums1[i]] = ht[nums1[i]] - 1
        else:
            for i in range(0, len(nums1)):
                if nums1[i] not in ht:
                    ht[nums1[i]] = 1
                else:
                    ht[nums1[i]] = ht[nums1[i]] + 1
            for i in range(0, len(nums2)):
                if nums2[i] in ht and ht[nums2[i]] > 0:
                    inter.append(nums2[i])
                    ht[nums2[i]] = ht[nums2[i]] - 1
        return inter