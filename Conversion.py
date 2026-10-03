from abc import ABC, abstractmethod
from typing import override

class Drone(ABC):
    ## def __init__(self, parameters)  is you constructor ##
    def __init__(self, manufacturer: str, year: int, carry_capacity: float):
        self.id: int = 0
        self._manufacturer = manufacturer
        self._year = year
        self._carry_capacity = carry_capacity
        self.next: Drone = None

## Getters( @property is the decorator for creating getters) ##
    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def year(self):
        return self._year

    @property
    def carry_capacity(self):
        return self._carry_capacity

    @property
    def id(self):
        return self._id

    @property
    def next(self):
        return self._next

    @abstractmethod
    def type(self):
        return self.type
## Setters ( @var.setter is the decorator for creating setters) ##
    @id.setter
    def id(self, value):
        self._id = value

    @next.setter
    def next(self, value):
        self._next = value
## @override is still similar to java, it is used to override the method of the parent class. ##
    @override
    def __str__(self):
        return f"\nID: {self.id}, Manufacturer: {self.manufacturer}, Year: {self.year}, Carry Capacity: {self.carry_capacity} kg"

class PriorityDrone(Drone):
    def __init__(self, manufacturer: str, year: int, carry_capacity: float):
        super().__init__(manufacturer, year, carry_capacity)

    @override
    def type(self):
        return "Priority"

    @override
    def __str__(self):
        return super().__str__() + f", Type: {self.type()}\n"

class StandardDrone(Drone):

    def __init__(self, manufacturer: str, year: int, carry_capacity: float):
        super().__init__(manufacturer, year, carry_capacity)

    @override
    def type(self):
        return "Standard"

    @override
    def __str__(self):
        return super().__str__() + f", Type: {self.type()}"

class Hanger:
    def __init__(self):
        self.droneInventory: list[Drone] = []
        self.droneCount: int = 1001
        self.maintenanceQueue: Drone = None
        self.droneMapById: dict[int, Drone] = {}
## def name(self, parameters) is how you define a method of the class ##
    def addDrone(self, drone: Drone):
        self.droneInventory.append(drone)
        drone.id = self.droneCount
        self.droneCount += 1

    def displayHangerInventory(self):
        if not self.droneInventory:
            print("Hanger is empty.")
        else:
            print("\nHanger Inventory:")
            for drone in self.droneInventory:
                print(drone)


if __name__ == "__main__":
    hanger = Hanger()
    hanger.displayHangerInventory()

## creating drone objects and adding them to the hanger inventory ##
    drones = [
        PriorityDrone("Northstar Robotics", 2025, 4.5),
        PriorityDrone("AeroWorks", 2024, 2.0),
        StandardDrone("Skyline Robotics", 2023, 8.0),
    ]

    for drone in drones:
        hanger.addDrone(drone)

    hanger.displayHangerInventory()