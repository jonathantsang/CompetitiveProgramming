class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ht = dict()
        same = []
        for ele in list1:
            if(ele in list2):
                same.append(ele)
        # Go through both saving index as dict value
        for i in range(0, len(list1)):
            if list1[i] in ht and list1[i] in same:
                ht[list1[i]] += i
            elif list1[i] in same:
                ht[list1[i]] = i
        for j in range(0, len(list2)):
            if list2[j] in ht and list2[j] in same:
                ht[list2[j]] += j
            elif list2[j] in same:
                ht[list2[j]] = j
        mini = 10001
        chose = []
        for place in ht.keys():
            if(ht[place] < mini):
                mini = ht[place]
        for place in ht.keys():
            if(ht[place] == mini):
                chose.append(place)
        return chose