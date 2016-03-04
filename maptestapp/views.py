from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

	addresslist = ['2376 Woodward Avenue, Lakewood, OH 44107']
	return render(request, 'test.html', { 'addresslist':addresslist} )
