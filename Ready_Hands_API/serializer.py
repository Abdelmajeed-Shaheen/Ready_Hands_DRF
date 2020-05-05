from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_permission
from .models import Client,Worker,Job ,Service,Applicant

class UserCreateSerializer(serializers.ModelSerializer):
	tokens = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name','last_name', 'tokens']
		extra_kwargs = {'password': {'write_only': True}}
	def get_tokens(self, user):
		tokens = RefreshToken.for_user(user)
		refresh = str(tokens)
		access = str(tokens.access_token)
		data = {"refresh": refresh,"access": access}
		return data

	def create(self, validated_data):
		user =User(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

class UserProfileSerializer(serializers.ModelSerializer):
	type = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ['username', 'first_name','last_name', 'type']
	def get_type(self,user):
		if has_permission(user, 'is_worker'):
			return 'is_worker'
		elif has_permission(user, 'is_client'):
			return 'is_client'
		return None

class WorkerSerializer(serializers.ModelSerializer):
	user = UserProfileSerializer()
	class Meta:
		model = Worker
		fields = ['user', 'image','phone_no', 'hour_rate','rating']

class ClientSerializer(serializers.ModelSerializer):
	user = UserProfileSerializer()
	class Meta:
		model = Client
		fields = ['user', 'image','phone_no']

class WorkerCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Worker
		exclude= ['user']

class ClientCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		exclude= ['user']

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		exclude= ['id']

class JobSerializer(serializers.ModelSerializer):
	client = ClientSerializer()
	service = ServiceSerializer()
	class Meta:
		model = Job
		fields='__all__'

class ApplicantSerializer(serializers.ModelSerializer):
	worker = WorkerSerializer()
	class Meta:
		model= Applicant
		exclude= ['job']

class JobCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model= Job
		exclude= ['client','status','service']

class ApplicantApplySerializer(serializers.ModelSerializer):
	class Meta:
		model = Applicant
		fields = '__all__'

class WorkerAppliedSerializer(serializers.ModelSerializer):
	job = JobSerializer()
	class Meta:
		model= Applicant
		exclude= ['worker']
