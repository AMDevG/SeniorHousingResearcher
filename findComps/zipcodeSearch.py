import pyzipcode
from .models import Providerinfo

def getNearbyZips(targetZip, searchRad):
    print("Zip being queried", targetZip)
    clean_list = []
    zipcodeDB = pyzipcode.ZipCodeDatabase()
    zipResults = [z.zip for z in zipcodeDB.get_zipcodes_around_radius(targetZip, searchRad)]

    return zipResults