# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import AccountManager, Account
# # Create your views here.
from django.shortcuts import render
from rest_framework import permissions, viewsets,views
from maptestapp.models import Account
from maptestapp.permissions import IsAccountOwner
from maptestapp.serializers import AccountSerializer
import geocoder
from geopy.distance import vincenty
from geopy.geocoders import Nominatim


def plot(request):
    coords = []
    lat_lng = []
    coordinate_pairs = []
    to_pass = []
    new_str = '['

    if request.method == 'POST':
        distance_selection = request.POST.get('sortOption', None)
        subject = request.POST.get('subject', None)
        addr1 = request.POST.get('addr1', None)
        addr2 = request.POST.get('addr2', None)
        addr3 = request.POST.get('addr3', None)
        addr4 = request.POST.get('addr4', None)
        addr5 = request.POST.get('addr5', None)
        addr6 = request.POST.get('addr6', None)
        addr7 = request.POST.get('addr7', None)
        addr8 = request.POST.get('addr8', None)
        addr9 = request.POST.get('addr9', None)


        print("Selection is ", distance_selection)


        if subject != '':
            coords.append(subject)
        if addr1!= '':
            coords.append(addr1)
        if addr2 != '':
            coords.append(addr2)
        if addr3 != '':
            coords.append(addr3)
        if addr4 != '':
            coords.append(addr4)
        if addr5 != '':
            coords.append(addr5)
        if addr6 != '':
            coords.append(addr6)
        if addr7 != '':
            coords.append(addr7)
        if addr8 != '':
            coords.append(addr8)
        if addr9 != '':
            coords.append(addr9)

        #print("List is ", coords)

    for address in coords:
        g = geocoder.google(address)
        coordinate_pair = str(g.latlng)
        coordinate_pair = coordinate_pair.replace('[',"")
        coordinate_pair = coordinate_pair.replace(']',"")
        coordinate_pair = coordinate_pair.split()
        coordinate_pairs.append(coordinate_pair)

    #print("Coordinate pairs are ", coordinate_pairs)

####CALCULATE DISTANCE BETWEEN POINTS######

#####################################################################################################################################
    
    if distance_selection == "distance":

        distance_dict = {}  #HOLDS LAT LNG WITH DISTANCE TO OBTAIN SORTED LIST FOR MARKING

        subject_address = coordinate_pairs[0]
        subject_str = subject_address[0].replace(",","") + ", " + subject_address[1].replace(",","")

        print(subject_str)

        for i in range(1, len(coordinate_pairs)):           ##ITERATES THROUGH COORD PAIRS PUTS DISTANCE INTO DICT
            target_address = coordinate_pairs[i]
            target_str = target_address[0].replace(",","") + ", " + target_address[1].replace(",","")
            distance = vincenty(subject_str, target_str).miles

            distance_dict[target_str] = distance

        sorted_pairs = sorted(distance_dict, key=lambda key: distance_dict[key])  ### CREATES SORTED LIST BY KEY
        sorted_pairs.insert(0,subject_str)

                                               ## APPEND SUBJECT PROPERTY AS FIRST ITEM IN SORTED LIST
        for item in sorted_pairs:
            split_coords = item.split()        ## FORMATS FOR JAVASCRIPT

            for i in range(0,len(sorted_pairs)):
                formatted = '{lat:'+split_coords[0]+' lng:'+split_coords[1] + '}'
                if formatted not in to_pass:
                    to_pass.append(formatted)

        for item in to_pass:
            new_str = new_str + item + ", "
            item = item.replace("'","")

        new_str = new_str +']'

        print ( "New String is ", new_str)

        return render(request, 'multiple.html', {'new_str':new_str})

#######################################################################################################################

    elif distance_selection == "order":

        sorted_pairs = []
        subject_address = coordinate_pairs[0]
        subject_str = subject_address[0].replace(",","") + ", " + subject_address[1].replace(",","")

        #print("Subject is ",subject_str)

        sorted_pairs.append(subject_str)


        for i in range(1, len(coordinate_pairs)):           ##ITERATES THROUGH COORD PAIRS PUTS DISTANCE INTO DICT
            target_address = coordinate_pairs[i]
            target_str = target_address[0].replace(",","") + ", " + target_address[1].replace(",","")
            print("Target string is ", target_str)
            print()
            sorted_pairs.append(target_str)

        #print("Sorted Pairs are ", sorted_pairs)


        for item in sorted_pairs:
            split_coords = item.split()        ## FORMATS FOR JAVASCRIPT

            for i in range(0,len(sorted_pairs)):
                formatted = '{lat:'+split_coords[0]+' lng:'+split_coords[1] + '}'
                if formatted not in to_pass:
                    to_pass.append(formatted)

                print("To Pass is ", to_pass)

        for item in to_pass:
            new_str = new_str + item + ", "
            item = item.replace("'","")

        new_str = new_str +']'

        print("New String is ", new_str)


        return render(request, 'multiple.html', {'new_str':new_str})

















def index(request):

    return render(request, 'index.html')

def signup(request):

	return render(request, 'signup.html')

def success(request):

	if request.method == 'POST':
		email_addr = request.POST.get('email')
		user_name = request.POST.get('username')
		email_list = [email_addr]
		Account.objects.create_user(email_addr, username=user_name)

	return render(request, 'success.html', {'email_list':email_list})


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


