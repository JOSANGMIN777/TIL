class Person:
    gene = 'xyz'
    
    
    def __init__(self, name):
        self.name = name
        
        
    def greeting(self):
        return(f'안녕, {self.name}')
        
        
class  mom(Person):
    gene = 'XX'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    def swim(self):
        return '엄마가 수영'
        
        
class dad(Person):
    gene = 'XY'
    
    def __init__(self, name):
            super().__init__(name)
            self.name = name
    
    def walk(self):
        return '아빠가 걷기'
        
        
        
class firstchild(mom, dad):
    Dad_gene = dad.gene
    
    
    def __init__(self, name):
            super().__init__(name)
            
    
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'    


baby1 = firstchild('아가')
print(baby1.cry()) #첫째가 응애
print(baby1.swim()) #첫째가 수영
print(baby1.walk()) #아빠가 걷기
print(baby1.gene) #super()를 썼고 mom이 먼저 상속되어 있으므로 만약 mom에 없으면 그다음순서인  dad에서 가져옴  xy를 가져옴 #person클래스에 염색체를 넣어도 가져오지않음.
print(baby1.Dad_gene) #xy
print(firstchild.mro()) #찾아올라가는 순서 