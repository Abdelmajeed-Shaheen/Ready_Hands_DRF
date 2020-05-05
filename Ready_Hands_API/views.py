from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
	HTTP_201_CREATED,HTTP_400_BAD_REQUEST, HTTP_200_OK
)
from .serializer import (
	UserCreateSerializer, WorkerSerializer, ApplicantSerializer,
	UserProfileSerializer, ServiceSerializer, ClientSerializer,
	WorkerCreateSerializer, ClientCreateSerializer, JobSerializer,
	JobCreateSerializer, WorkerAppliedSerializer
)
from .models import Worker, Client , Job , Service ,Applicant
from .permissions import IsClient ,IsWorker
from rolepermissions.checkers import has_permission
from rolepermissions.roles import assign_role
from datetime import datetime


class RegisterAPI(CreateAPIView):
	serializer_class = UserCreateSerializer


class WorkerCreateAPI(APIView):
	def post(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		serializer = WorkerCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			user = User.objects.get(username= request.user.username)
			# request.user instead of grabbing user object
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
			# request.user instead of grabbing user object
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
			return Response(serializer.data, status=status.HTTP_200_OK)
		elif has_permission(request.user, 'is_client'):
			client = Client.objects.get(user=request.user)
			serializer = ClientSerializer(client)
			return Response(serializer.data, status=status.HTTP_200_OK)
		serializer = UserProfileSerializer(request.user)
		return Response({'user':serializer.data}, status=status.HTTP_200_OK)


class JobAPI(APIView):
	def get(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		jobs = Job.objects.filter(date_to__gte=datetime.today(), status="P")
		serializer = JobSerializer(jobs,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class ClientJobAPI(APIView):
	def get(self,request):
		self.permission_classes = [IsAuthenticated,IsClient]
		self.check_permissions(request)
		jobs = Job.objects.filter(client=request.user.client)
		serializer = JobSerializer(jobs,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class JobApplicants(APIView):
	def get(self,request,job_id):
		self.permission_classes = [IsAuthenticated,IsClient]
		self.check_permissions(request)
		applicants = Applicant.objects.filter(job_id=job_id)
		serializer = ApplicantSerializer(applicants,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceAPI(APIView):
	def get(self,request):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		services = Service.objects.all()
		serializer = ServiceSerializer(services,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class CreateJobAPI(APIView):
	def post(self,request):
		self.permission_classes = [IsAuthenticated,IsClient]
		self.check_permissions(request)
		serializer = JobCreateSerializer(data=request.data)
		if serializer.is_valid():
			service = Service.objects.get(title=request.data['service'])
			serializer.save(client=request.user.client, service= service)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ApplyToJob(APIView):
	def post(self,request,job_id):
		self.permission_classes = [IsAuthenticated,IsWorker]
		self.check_permissions(request)
		try:
			applicant = Applicant(worker=request.user.worker,job_id=job_id)
			applicant.save()
			return Response(
				{'msg':'Your application has been submited.'},
				status=status.HTTP_201_CREATED
			)
		except:
			return Response(
				{'msg':'Something went wrong, please try again!'},
				status=status.HTTP_400_BAD_REQUEST
			)

class WorkerAppliedJobs(APIView):
	def get(self,request):
		self.permission_classes = [IsAuthenticated,IsWorker]
		self.check_permissions(request)
		appliedJobs= Applicant.objects.filter(worker=request.user.worker)
		serializer = WorkerAppliedSerializer(appliedJobs,many=True)
		return Response(serializer.data)
