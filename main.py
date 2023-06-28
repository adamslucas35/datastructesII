"""
Adam S Lucas
ID: 010241173
"""

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

    # load package csv into hashtable
    loadPackageCSV("C950_ALUC167_DOCS/WGUPS_Package.csv", packageHashTable)

    # array of all id for all packages
    packageIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                  29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

    # packages to be manually loaded onto each truck following special constraints
    packagesForTruck1 = [13, 14, 15, 16, 19, 20, 29, 1, 30, 31, 40, 37, 34]
    packagesForTruck2 = [3, 18, 36, 38, 28, 6, 32, 25, 27, 35, 2, 33, 8, 26]
    packagesForTruck3 = [9, 7, 39, 11, 17, 12, 21, 4, 5, 23, 10, 22, 24]
    hub = "4001 South 700 East (84107)"

    # initiating trucks
    truck1 = Truck(1, 18, 16, None, hub, datetime.timedelta(hours=8), packagesForTruck1, 0.0)
    truck2 = Truck(2, 18, 16, None, hub, datetime.timedelta(hours=9, minutes=5),
                   packagesForTruck2, 0.0)
    truck3 = Truck(3, 18, 16, None, hub, datetime.timedelta(hours=10, minutes=20),
                   packagesForTruck3, 0.0)

    # function to return the distance between to points on distances table csv
    def findDistance(index1, index2):
        distance = distanceData[index1][index2]
        if distance == '':
            distance = distanceData[index2][index1]
        return float(distance)

    # function to return index of string address format: "address (zip)"
    def returnAddress(address):
        for i, item in enumerate(addressData):
            if item[0] == address:
                return i

    # function to update the status of the package, whether is has been delivered, on route, or at hub
    def checkStatus(package, time):
        # if entered time is after delivery time
        if package.departure < time and time > package.delivered:
            package.status = "DELIVERED"
        # if entered time is after departure from hub and before the package has been delivered
        elif time > package.departure and time < package.delivered:
            package.status = "ON THE WAY"
        # if package has not left the hub yet
        else:
            package.status = "HUB"

    # function to start movement of truck and deliver the package
    def delivery(truckObject):
        # create array of undelivered packages, filled up by packages that have been preloaded onto the truck
        undeliveredPackages = []
        for packageId in truckObject.packages:
            package = packageHashTable.get(str(packageId))
            undeliveredPackages.append(package)
        truckObject.packages.clear()
        # while packages are still on truck look for closest address based on loaded packages
        while len(undeliveredPackages) > 0:
            nextAddress = 10000
            nextPackage = None
            for pack in undeliveredPackages:
                packAddress = f"{pack.address} ({pack.zip})"
                mileage = findDistance(returnAddress(truckObject.currentAddress), returnAddress(packAddress))
                if mileage <= nextAddress:
                    nextAddress = mileage
                    nextPackage = pack
            # add delivered packages to truck to keep track of what has been delivered prior
            truckObject.packages.append(nextPackage.id)
            # once delivered remove from undelivered array
            undeliveredPackages.remove(nextPackage)
            # add up the mileage
            truckObject.mileage += nextAddress
            # set up next address search
            nextCombinedAddress = f"{nextPackage.address} ({nextPackage.zip})"
            truckObject.currentAddress = nextCombinedAddress
            # set delivery time which is in constant increase once truck leaves hub
            truckObject.travelTime += datetime.timedelta(hours=nextAddress / 18)
            # set departure of package to state it is on the way
            nextPackage.departure = truckObject.departureTime
            # set delivery time of package to state it has been delivered
            nextPackage.delivered = truckObject.travelTime
        # returns the truck to the hub after delivery of all packages
        returnHub = findDistance(returnAddress(truckObject.currentAddress), returnAddress(hub))
        truckObject.mileage += returnHub
        truckObject.currentAddress = hub

    # function that runs console interface
    def runProgram():
        # start deliveries
        delivery(truck1)
        delivery(truck2)
        # truck 1 returns at 9:32, and truck3 does not leave until 10:20 so there are never more than 2 drivers out
        # and about
        delivery(truck3)
        print("WELCOME TO MY DELIVERY SYSTEM!")
        print("-------------------------------")
        # displays total milage traveled by all three trucks
        print("TOTAL MILES TRAVELED: ", truck1.mileage + truck2.mileage + truck3.mileage)
        print("-------------------------------")
        # takes input of time in HH:MM format to see where all packages are
        time = input("Enter time in HH:MM format to see the status of all packages:\n")
        # makes sure the time entered is in the correct format, if not, exits
        try:
            (hour, minute) = time.split(":")
            inputTime = datetime.timedelta(hours=int(hour), minutes=int(minute))
            for pId in range(1, 41):
                packages = packageHashTable.get(str(pId))
                checkStatus(packages, inputTime)
                print(packages)
            # print distance traveled of each truck
            print(f"TRUCK 1 traveled: {truck1.mileage} miles.")
            print(f"TRUCK 2 traveled: {truck2.mileage} miles.")
            print(f"TRUCK 3 traveled: {truck3.mileage} miles.")

        except ValueError:
            print("Incorrect, please run program again.")


    # begins program
    runProgram()
