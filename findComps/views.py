from django.shortcuts import render


def find(request):
	return render(request, 'comps/findSNFs.html' )