class OneIndexedList:
    
    def __init__(self, lst = None):
        if lst is None:
            lst = []
        self.lst = lst

    def __getitem__(self, key):
        return self.lst[key-1]
        
    def __setitem__(self, key, value):
        self.lst[index-1] = self.value

    def append(self, value):
        self.lst.append(value)


 
        
