import csv
import datetime

from truck import Truck
from csvLoader import loadPackageCSV
from hasher import HashTable

if __name__ == '__main__':
    # open tables
    # read distance data list
    with open("C950_ALUC167_DOCS/WGUPS_Distances.csv") as distanceTable:
        distanceData = list(csv.reader(distanceTable, delimiter=','))
        # distance_data = convertDistanceToFloat(distanceData)
    # address data list
    with open("C950_ALUC167_DOCS/WGUPS_Addresses.csv") as addressTable:
        addressData = list(csv.reader(addressTable))
    # package data list
    with open("C950_ALUC167_DOCS/WGUPS_Package.csv") as packageTable:
        packageData = list(csv.reader(packageTable, delimiter=','))

    # initiate and implement hashTable
    packageHashTable = HashTable()

    loadPackageCSV("C950_ALUC167_DOCS/WGUPS_Package.csv", packageHashTable)

    packagesForTruck1 = [7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26]
    packagesForTruck2 = [1, 3, 13, 14, 15, 16, 18, 19, 20, 29, 30, 31, 34, 36, 37, 38]
    packagesForTruck3 = [2, 4, 5, 6, 25, 27, 28, 32, 33, 35, 39, 40]

    # initiating trucks (addressData[0] = hub address "4001 South 700 East (84107)")
    truck1 = Truck(1, 18, 16, None, "4001 South 700 East (84107)", datetime.timedelta(hours=10, minutes=20),
                   packagesForTruck1, 0.0)
    truck2 = Truck(2, 18, 16, None, "4001 South 700 East (84107)", datetime.timedelta(hours=8, minutes=0),
                   packagesForTruck2, 0.0)
    truck3 = Truck(3, 18, 16, None, "4001 South 700 East (84107)", datetime.timedelta(hours=9, minutes=5),
                   packagesForTruck3, 0.0)


    # def distanceFinder(address1, address2):
    #     distance = distanceData[address1][address2]
    #     if distance == "":
    #         distance = distanceData[address2][address1]
    #     return distance
    #


    def findDistance(index1, index2):
        distance = distanceData[index1][index2]
        if distance == '':
            distance = distanceData[index2][index1]
        return float(distance)


    def returnAddress(address):
        for i, item in enumerate(addressData):
            if item[0] == address:
                return i

    point1 = (returnAddress(truck1.currentAddress))
    point2 = (returnAddress("3595 Main St (84115)"))
    print(findDistance(point1, point2))

    def delivery(truckObject):
        undeliveredPackages = []
        for packageId in truckObject.packages:
            package = packageHashTable.get(str(packageId))
            undeliveredPackages.append(package)
        truckObject.packages.clear()
        while len(undeliveredPackages) > 0:
            nextAddress = 10000
            nextPackage = None
            for pack in undeliveredPackages:
                packId = pack.id
                packAddress = f"{pack.address} ({pack.zip})"
                mileage = findDistance(returnAddress(truckObject.currentAddress), returnAddress(packAddress))
                if mileage <= nextAddress:
                    nextAddress = mileage
                    nextPackage = pack
            truckObject.packages.append(nextPackage.id)
            undeliveredPackages.remove(nextPackage)
            truckObject.mileage += mileage
            nextCombinedAddress = f"{nextPackage.address} ({nextPackage.zip})"
            truckObject.currentAddress = nextCombinedAddress
            truckObject.travelTime = datetime.timedelta(hours=nextAddress / truckObject.truckSpeed)
            nextPackage.delivered = datetime.timedelta(hours=nextAddress / truckObject.truckSpeed)
            nextPackage.departureTime = truckObject.departureTime

            print("Delivering Package:", nextPackage.id)
            print("Current Address:", nextPackage.address)
            print("Updated Truck Information:", truckObject)
            nextPackage.checkStatus(nextPackage.delivered)
            print(nextPackage)
            print("---")


    delivery(truck1)
    delivery(truck2)
    delivery(truck3)
