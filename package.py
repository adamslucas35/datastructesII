import datetime
from truck import Truck

class Package:
    def __init__(self, id, address, deadline, city, zip, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.status = status
        self.departure = None
        self.delivered = None

    def __str__(self):
        return f"{self.id}, {self.address}, {self.deadline}, {self.city}, {self.zip}, {self.weight}, {self.departure} -- {self.delivered}, {self.status}"
