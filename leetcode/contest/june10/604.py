class StringIterator:
    counter = 0
    amount = ""
    cs = ""
    leng = 0
    index = 0
    char = ""

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.index = 0
        self.counter = 0
        self.amount = ""
        self.cs = compressedString
        self.leng = len(compressedString)
        self.char = ""
        # Form amount and string
        i = self.index
        while(i < self.leng):
            self.char = compressedString[i]
            stringnum = ""
            i += 1
            while(not compressedString[i].isalpha()):
                stringnum += compressedString[i]
                i += 1
            break
        self.amount = int(stringnum)

    def next(self):
        """
        :rtype: str
        """
        if(self.index >= self.leng):
            return " "
        elif(self.counter < self.amount):
            self.counter += 1
            print(self.char)
            return self.char
        else:
            # Form amount and string
            while(self.index < self.leng):
                self.char = self.cs[self.index]
                stringnum = ""
                self.index += 1
                while(not self.cs[self.index].isalpha()):
                    stringnum += self.cs[self.index]
                    self.index += 1
                break
            self.amount = int(stringnum)
            print(self.char)
            return self.char
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if(self.index >= self.leng):
            return False
        elif(self.counter < self.amount):
            return True
        else:
            while(self.index < self.leng):
                self.char = self.cs[self.index]
                stringnum = ""
                self.index += 1
                while(not self.cs[self.index].isalpha()):
                    stringnum += self.cs[self.index]
                    self.index += 1
                break
            self.amount = int(stringnum)
            return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()