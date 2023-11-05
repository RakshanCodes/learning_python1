class Room:
    def __init__(self, name, length, breath, items):
        print("__init__", name)
        self.name = name
        self.breath = breath
        self.length = length
        self.items = items

    def area(self):
        return self.breath * self.length

    def add_item(self, item):
        self.items.append(item)

    def print_info(self):
        print(
            f"Info of room '{self.name}' is: area={self.area()} items={self.items}"  # noqa: E501
        )


class BedRoom(Room):
    def __init__(self, name, length, breath):
        super(BedRoom, self).__init__(
            f"{name} bedroom", length, breath, ["bed"])

    
class BathRoom(Room):
    def __init__(self, name, length, breath):
        super(BathRoom, self).__init__(
            f"{name} bathroom", length, breath, ["bucket"])


r1 = BedRoom("master", 20, 12)
r1.add_item("table")
r1.print_info()

r2 = BathRoom("master", 40, 40)
r2.print_info()
