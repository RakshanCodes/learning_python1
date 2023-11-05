class Bikes:
    def __init__(self, name, color, cost, items):
        self.name = name
        self.cost = cost
        self.color = color
        self.items = items

    def add_items(self, items):
        self.items.append(items)


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
        super(BMW, self).__init__(f"{__name__} {name} BMW", "Red", cost, ["BMW"])


# v1 = Highness("Favourite")
v2 = BMW("Dave's Bike", color="Green")

if __name__ == '__main__':
    # v1.add_items("double seater")
    # print(v1.items)
    print(v2.name)
