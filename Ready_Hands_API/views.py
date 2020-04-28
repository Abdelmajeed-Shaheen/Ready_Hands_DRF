from decimal import Decimal
from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from  .models import Worker, Client

@api_view(['POST'])
def RegisterAPI(request):
	#check if data is recieved
	if( not request.data):
		return Response({'data':f'data is undifiend'}, status=status.HTTP_400_BAD_REQUEST)
	#check if username is recieved
	if not 'username' in request.data:
		return Response({'username':f'username is requierd'}, status=status.HTTP_400_BAD_REQUEST)
	#check if username already exist
	if(User.objects.filter(username=request.data['username'])):
		return Response({'username':f'username alreadyexist'}, status=status.HTTP_400_BAD_REQUEST)
	#check if other fields exist
	if('first_name' in request.data and
	'last_name'in request.data and
	'password'in request.data and
	'phone_no'in request.data and
	'type'in request.data):
		newuser= User(username = request.data['username'],
		first_name= request.data['first_name'],
		last_name=request.data['last_name'])
		newuser.set_password(request.data['password'])
		#check if worker or client
		if request.data['type']=='worker':
			#check if hour_rate exist
			if not 'hour_rate'in request.data:
				return Response({'hour_rate':f'hour rate is requiered'}, status=status.HTTP_400_BAD_REQUEST)
			newuser.save()
			newworker= Worker(user=newuser,
			phone_no = request.data['phone_no'],
			hour_rate = Decimal(request.data['hour_rate']))
			newworker.save()
		else:
			newuser.save()
			newclient = Client(user=newuser,
			phone_no = request.data['phone_no'])
			newclient.save()
		tokens = RefreshToken.for_user(newuser)
		refresh = str(tokens)
		access = str(tokens.access_token)
		data = {
			"refresh": refresh,
			"access": access
		}
		return Response(data, status=status.HTTP_200_OK)
	else:
		return Response({'data':f'data is incompleted'}, status=status.HTTP_400_BAD_REQUEST)
