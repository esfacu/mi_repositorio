#constructor int
# __init__

class Vector:
    def __init__(self, data) -> None:
        self.data = data
        
    def __str__(self) -> str:
        return f"El valor de este verctor es: {self.data}"
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, pos):
        return self.data[pos]
    
    def __setitem__(self, pos, value):
        self.data[pos] = value 
        
    def __iter__(self):
        for pos in range(0,len(self.data)):
            yield f"Value[{pos}]: {self.data[pos]}"
    
vector = Vector([1,2,3])
for i in vector:
    print(i)