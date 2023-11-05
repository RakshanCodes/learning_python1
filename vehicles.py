class Bikes:
    def _init_(self,name,color,cost,items):
        print("_init_",name)
        self.name = name
        self.cost = cost
        self.color= color
    def items(self):
        return self.items
    def add_items(self,items):
        self.items.append(items)
    def cost(self):
        return self.cost
    def name(self):
        return self.name
    def color(self):
        return self.color
class highness(Bikes):
    def __init__(self, name,):
        super(highness,self,)._init_(
            f"{name} Honda highness", ["Honda"])
        
class BMW(Bikes):
    def __init__(self, name):
        super(BMW,self)._init_(
            f"{name} BMW",["BMW"])
        
v1=highness("Favourite")
v1.add_items("double seater")
v1()

v2=BMW("Second favourite")
v2.add_items("single seater")
v2()


        
        
    
        
            
        
        
        
        
        
        
        
        
        
        