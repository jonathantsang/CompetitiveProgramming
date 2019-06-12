class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        contains = {} # key: file contents, value: paths to the file
        for file in paths:
            name = file.split()
            path = name[0]
            # print(name)
            for i in range(1, len(name)):
                filename = name[i].split('(')[0]
                contents = name[i].split('(')[1][:-1]
                # print(path, filename, contents)
                if contents in contains:
                    contains[contents].append(path + '/' + filename)
                else:
                    contains[contents] = [path + '/' + filename]
        soln = []
        for content in contains:
            if len(contains[content]) == 1:
                continue
            duplicates = []
            for path in contains[content]:
                duplicates.append(path)
            soln.append(duplicates)
        return soln