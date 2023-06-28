from package import Package
import csv


# takes the package csv file and inserts the data into the hashtable while also creating a package object for each
# item sorted by index
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
