import pyzipcode

def getNearbyZips(targetZip, searchRad):
    clean_list = []
    zipcodeDB = pyzipcode.ZipCodeDatabase()
    zipResults = [z.zip for z in zipcodeDB.get_zipcodes_around_radius(targetZip, searchRad)]
    return zipResults