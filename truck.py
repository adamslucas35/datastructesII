class Truck:

    def __init__(self, id, truckSpeed, loadCapacity, currentLoad, currentAddress, departureTime, packages, mileage):
        self.id = id
        self.truckSpeed = truckSpeed  # 18mph
        self.loadCapacity = loadCapacity
        self.currentLoad = currentLoad
        self.currentAddress = currentAddress
        self.departureTime = departureTime
        self.packages = packages
        self.mileage = mileage
        self.travelTime = departureTime

    def __str__(self):
        return f"{self.id}, {self.currentAddress}, {self.packages}, {self.mileage}"
