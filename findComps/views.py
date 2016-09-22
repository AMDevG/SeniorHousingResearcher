from django.shortcuts import render
from .zipcodeSearch import getNearbyZips
from .models import Providerinfo

def find(request):
	return render(request, 'comps/findSNFs.html' )


def compsearch(request):

	facility_information = {}
	comp_objects =[]
	flat_objects = []

	if request.method == 'POST':
		zipcode = request.POST.get('zip', None)
		print("zipcode received ", zipcode)
		radius = request.POST.get('radius', None)
		zips = getNearbyZips(zipcode, radius)

		for zipcode in zips:
			addition = Providerinfo.objects.all().filter(zip=zipcode)	# returns QuerySet Object
			comp_objects.append(addition)
		print("Length of comp_objects is ", len(comp_objects))
		

	counter = 0
	while counter != len(comp_objects):				##FLATTENS INTO STRAIGHT LIST
		item = comp_objects[counter]
		for i in item:
			flat_objects.append(i)
		counter+=1

	
	for item in flat_objects:
		facility_information[item.provname] = {}
		clean_provname = item.provname
		clean_comp_address = item.address
		clean_comp_city = item.city
		clean_comp_state = item.state
		clean_comp_zip = item.zip
		clean_comp_phone = item.phone
		clean_comp_bedcert = item.bedcert
		clean_comp_ownertype = item.ownership
		clean_comp_ownername = item.owner_name

		facility_information[item.provname]['address'] = clean_comp_address
		facility_information[item.provname]['city'] = clean_comp_city
		facility_information[item.provname]['state'] = clean_comp_state
		facility_information[item.provname]['zip'] = clean_comp_zip
		facility_information[item.provname]['phone'] = clean_comp_phone
		facility_information[item.provname]['bedcert'] = clean_comp_bedcert
		facility_information[item.provname]['ownertype'] = clean_comp_ownertype
		#facility_information[item.provname]['ownername'] = clean_comp_ownername   ####NEED TO MIGRATE OVER FROM OTHER TABLE 

		
	print(facility_information)

	return render(request, 'comps/findSNFs.html' )