class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        storage = dict()
        # Files in array
        for files in paths:
            content = files.split(" ")
            path = content[0]
            # Files in directory
            for i in range(1, len(content)):
                filename = content[i][0:len(content[i])].split("(")[0]
                contents = content[i][0:len(content[i])].split("(")[1]
                contents = contents[:len(contents)-1]
                if contents not in storage:
                    storage[contents] = []
                    storage[contents].append(path+"/"+filename)
                else:
                    storage[contents].append(path+"/"+filename)

        final = []
        for key in storage.keys():
            if(len(storage[key]) >= 2):
                final.append(storage[key])
        return final    