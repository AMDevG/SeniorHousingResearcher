from django.shortcuts import render

from .zipcodeSearch import getNearbyZips


def find(request):
	return render(request, 'comps/findSNFs.html' )


def compsearch(request):

	if request.method == 'POST':
		zipcode = request.POST.get('zip', None)
		print("zipcode received ", zipcode)
		radius = request.POST.get('radius', None)
		zips = getNearbyZips(zipcode, radius)

		print(zips)

	return render(request, 'comps/findSNFs.html' )