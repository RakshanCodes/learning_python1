class Bikes:
    def __init__(self, name, color, cost, items):
        print("_init_", name)
        self.name = name
        self.cost = cost
        self.color = color
        self.items = items

    def add_items(self, items):
        self.items.append(items)

    # def cost(self):
    #     return self.cost


class Highness(Bikes):
    def __init__(
        self,
        name,
    ):
        super(
            Highness,
            self,
        ).__init__(f"{name} Honda Highness", "Blue", 2312, ["Honda"])


class BMW(Bikes):
    def __init__(self, name, cost = 2412, color = "Red"):
        super(BMW, self).__init__(f"{name} BMW", "Red", cost, ["BMW"])


v1 = Highness("Favourite")
v1.add_items("double seater")
print(v1.items)

v2 = BMW("Second favourite", color="Green")
v2.add_items("single seater")
print(v2.cost)
