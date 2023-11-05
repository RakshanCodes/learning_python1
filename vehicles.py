class Bikes:
    def _init_(self,name,color,cost):
        print("_init_",name)
        self.name = name
        self.cost = cost
        self.color= color
    def cost(self):
        return self.cost
    def name(self):
        return self.name
    def color(self):
        return self.color
class highness(Bikes):
    def __init__(self, name, color, cost):
        super(highness,self)._init_(
            f"{name} Honda highness",cost,color ["Honda"])
class BMW(Bikes):
    def __init__(self, name, color, cost):
        super(BMW,self)._init_(
            f"{name} BMW",cost,color ["BMW"])
        
        
    
        
            
        
        
        
        
        
        
        
        
        
        