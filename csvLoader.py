from package import Package
import csv


def loadPackageCSV(fileName, newHashTable):
    with open(fileName) as packageDestinations:
        packageInfo = csv.reader(packageDestinations, delimiter=',')
        next(packageInfo)
        next(packageInfo)
        for package in packageInfo:
            packageId = package[0]
            address = package[1]
            city = package[2]
            deadline = package[5]
            zipcode = package[4]
            weight = package[6]
            status = "HUB"

            package = Package(packageId, address, deadline, city, zipcode, weight, status)
            newHashTable.insert(packageId, package)


def delivery(truckObject):
    undeliveredPackages = []
    for packageId in truckObject.packages:
        undeliveredPackages.append(packageId)
    truckObject.packages.clear()
    truckAddress = returnAddress(truckObject.currentAddress)
    while len(undeliveredPackages) > 0:
        nextAddress = 10000
        nextPackage = None
        for p in undeliveredPackages:
            pId = int(p)
            if float(findDistance(truckAddress, pId)) <= nextAddress:
                nextAddress = float(findDistance(truckAddress, pId))
                nextPackage = p
        truckObject.packages.append(nextPackage.id)
        undeliveredPackages.remove(nextPackage)
        truckObject.mileage += nextAddress
        truckObject.currentAddress = nextPackage.address
        truckObject.travelTime += datetime.timedelta(hours=nextAddress / 18)
        nextPackage.delivered = datetime.timedelta(hours=nextAddress / 18)
        nextPackage.departureTime = truckObject.departureTime

        print("Delivering Package:", nextPackage.id)
        print("Current Address:", nextPackage.address)
        print("Updated Truck Information:", truckObject)
        nextPackage.checkStatus(nextPackage.delivered)
        print(nextPackage)
        print("---")
