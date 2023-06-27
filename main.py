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

    packageIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                  29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

    packagesForTruck1 = [13, 14, 15, 16, 19, 20, 29, 1, 30, 31, 40, 37, 34]
    packagesForTruck2 = [3, 18, 36, 38, 28, 6, 32, 25, 27, 35, 2, 33, 8, 26]
    packagesForTruck3 = [9, 7, 39, 11, 17, 12, 21, 4, 5, 23, 10, 22, 24]


    # initiating trucks
    truck1 = Truck(1, 18, 16, None, "4001 South 700 East (84107)", datetime.timedelta(hours=8), packagesForTruck1, 0.0)
    truck2 = Truck(2, 18, 16, None, "4001 South 700 East (84107)", datetime.timedelta(hours=9, minutes=5),
                   packagesForTruck2, 0.0)
    truck3 = Truck(3, 18, 16, None, "4001 South 700 East (84107)", datetime.timedelta(hours=10, minutes=20),
                   packagesForTruck3, 0.0)


    def findDistance(index1, index2):
        distance = distanceData[index1][index2]
        if distance == '':
            distance = distanceData[index2][index1]
        return float(distance)


    def returnAddress(address):
        for i, item in enumerate(addressData):
            if item[0] == address:
                return i

    def checkStatus(package, time):
        if package.departure < time and time > package.delivered:
            package.status = "DELIVERED"
        elif time > package.departure and time < package.delivered:
            package.status = "ON THE WAY"
        else:
            package.status = "HUB"


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
                packAddress = f"{pack.address} ({pack.zip})"
                mileage = findDistance(returnAddress(truckObject.currentAddress), returnAddress(packAddress))
                if mileage <= nextAddress:
                    nextAddress = mileage
                    nextPackage = pack
            truckObject.packages.append(nextPackage.id)
            undeliveredPackages.remove(nextPackage)
            truckObject.mileage += nextAddress
            nextCombinedAddress = f"{nextPackage.address} ({nextPackage.zip})"
            truckObject.currentAddress = nextCombinedAddress
            truckObject.travelTime += datetime.timedelta(hours=nextAddress / 18)
            nextPackage.departure = truckObject.departureTime
            nextPackage.delivered = truckObject.travelTime
            print(nextPackage.departure, "-departure")
            print(nextPackage.delivered, "-delivered")

            nextPackage.departure = truckObject.departureTime

            # print("Delivering Package:", nextPackage.id)
            # print("Current Address:", nextPackage.address)
            # print("Updated Truck Information:", truckObject)
            # print(nextPackage)
            # print("---")


    def runProgram():
        delivery(truck1)
        delivery(truck2)
        delivery(truck3)
        print("WELCOME TO MY DELIVERY SYSTEM!")
        print("-------------------------------")
        print("TOTAL MILES TRAVELED: ", truck1.mileage + truck2.mileage + truck3.mileage)
        print("-------------------------------")
        time = input("Enter time in HH:MM format to see the status of all packages:\n")
        try:
            (hour, minute) = time.split(":")
            inputTime = datetime.timedelta(hours=int(hour), minutes=int(minute))
            for pId in range(1, 41):
                packages = packageHashTable.get(str(pId))
                checkStatus(packages, inputTime)
                print(packages)
            print("TOTAL MILES TRAVELED at inputted time: ", truck1.mileage + truck2.mileage + truck3.mileage)
        except ValueError:
            print("Incorrect, please run program again.")




    runProgram()



