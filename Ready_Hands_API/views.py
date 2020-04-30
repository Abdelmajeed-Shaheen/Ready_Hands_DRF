from .serializer import UserCreateSerializer,WorkerSerializer,ServiceSerializer,ClientSerializer,WorkerCreateSerializer,ClientCreateSerializer,JobSerializer
from .models import Worker, Client , Job , Service
from rolepermissions.roles import assign_role
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rolepermissions.checkers import has_permission

class RegisterAPI(CreateAPIView):
	serializer_class = UserCreateSerializer
	print("================================================11111111111")


class WorkerCreateAPI(APIView):
	def post(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		serializer = WorkerCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			user = User.objects.get(username= request.user.username)
			assign_role(user, 'worker')
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ClientCreateAPI(APIView):
	def post(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		serializer = ClientCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			user = User.objects.get(username= request.user.username)
			assign_role(user, 'client')
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
	def get(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		if has_permission(request.user, 'is_worker'):
			worker = Worker.objects.get(user=request.user)
			serializer = WorkerSerializer(worker)
			return Response(serializer.data)
		elif has_permission(request.user, 'is_client'):
			client = Client.objects.get(user=request.user)
			serializer = ClientSerializer(client)
			return Response(serializer.data)


class JobAPI(APIView):
	def get(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		jobs = Job.objects.all()
		serializer = JobSerializer(jobs,many=True)
		return Response(serializer.data)


class ServiceAPI(APIView):
	def get(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		services = Service.objects.all()
		serializer = ServiceSerializer(services,many=True)
		return Response(serializer.data)
