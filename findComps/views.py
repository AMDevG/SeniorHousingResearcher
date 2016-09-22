from django.shortcuts import render
from .zipcodeSearch import getNearbyZips
from .models import Providerinfo

import json
import requests
import simplejson

def find(request):
	return render(request, 'comps/findSNFs.html' )

def getDistance(subject_address, temp_address):
	try:
		print("GETTING GOOGLE DISTANCE")
		url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+subject_address+"&destinations="+temp_address+"&key=AIzaSyABAGhtae7h91pf24nfyZ6eFiPThWW3W4M"
		result = requests.get(url)
		data = json.loads(result.text)
		distance = data['rows'][0]['elements'][0]['distance']['text']
		return distance
	except:
		return None

def compsearch(request):

	

	counter = 0
	facility_information = {}
	comp_objects =[]
	flat_objects = []

	if request.method == 'POST':
		subject_address = request.POST.get('subj_addr', None)
		zipcode = request.POST.get('zip', None)
		radius = request.POST.get('radius', None)

		zips = getNearbyZips(zipcode, radius)

		for zipcode in zips:
			addition = Providerinfo.objects.all().filter(zip=zipcode)	# returns QuerySet Object
			comp_objects.append(addition)
	
	while counter != len(comp_objects):				##FLATTENS INTO STRAIGHT LIST
		item = comp_objects[counter]
		for i in item:
			flat_objects.append(i)
		counter+=1

	for item in flat_objects:
		facility_information[item.provname] = {}	## Creates initial dictionary, key is facil name: holds another dic with data
		
		clean_provname = item.provname
		clean_comp_address = item.address
		clean_comp_city = item.city
		clean_comp_state = item.state
		clean_comp_zip = item.zip
		clean_comp_phone = item.phone
		clean_comp_bedcert = item.bedcert
		clean_comp_ownertype = item.ownership
		#clean_comp_ownername = item.owner_name

		subject_address = subject_address.strip().replace(" ","")

		full_address = clean_comp_address + clean_comp_city + clean_comp_state + clean_comp_zip
		full_address = full_address.strip().replace(" ","")


		distance_from_subject = getDistance(subject_address, full_address)

		print("Calculated Distance is: ", distance_from_subject)

		facility_information[item.provname]['address'] = clean_comp_address
		facility_information[item.provname]['city'] = clean_comp_city
		facility_information[item.provname]['state'] = clean_comp_state
		facility_information[item.provname]['zip'] = clean_comp_zip
		facility_information[item.provname]['phone'] = clean_comp_phone
		facility_information[item.provname]['bedcert'] = clean_comp_bedcert
		facility_information[item.provname]['ownertype'] = clean_comp_ownertype
		facility_information[item.provname]['distance'] = distance_from_subject
		#facility_information[item.provname]['ownername'] = clean_comp_ownername   ####NEED TO MIGRATE OVER FROM OTHER TABLE 

	return render(request, 'comps/compResults.html', {'facility_information': facility_information})