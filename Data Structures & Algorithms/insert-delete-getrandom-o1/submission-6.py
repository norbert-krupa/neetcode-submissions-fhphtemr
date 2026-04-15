class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indexMap = {} # val : index
        

    def insert(self, val: int) -> bool:
        if val not in self.indexMap:
            self.values.append(val)
            self.indexMap[val] = len(self.values) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.indexMap:
            index = self.indexMap[val]
            self.values[index] = self.values[-1]
            if val != self.values[-1]:
                self.indexMap[self.values[-1]] = index
            del self.indexMap[val]
            self.values.pop()
            return True
        else:
            return False
            
        
    def getRandom(self) -> int:
        return self.values[random.randint(0, len(self.values)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()