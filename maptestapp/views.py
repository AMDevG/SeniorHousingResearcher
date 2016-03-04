# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import AccountManager, Account
# # Create your views here.
from django.shortcuts import render
from rest_framework import permissions, viewsets,views

from maptestapp.models import Account
from maptestapp.permissions import IsAccountOwner
from maptestapp.serializers import AccountSerializer
from .import views


def home(request):


	addresslist = ['2376 Woodward Avenue, Lakewood, OH 44107']
	return render(request, 'test.html', { 'addresslist':addresslist} )

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


