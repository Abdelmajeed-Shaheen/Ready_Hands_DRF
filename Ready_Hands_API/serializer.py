from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Client

def get_tokens_for_user(user):
	refresh = RefreshToken.for_user(user)

	return {
		'refresh': str(refresh),
		'access': str(refresh.access_token),
	}

class UserSerializer(serializers.ModelSerializer):
	tokens = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = ('username', 'password', 'first_name','last_name','phone_no', 'tokens')
		extra_kwargs = {'password': {'write_only': True}}


	def get_tokens(self, user):
		tokens = RefreshToken.for_user(user)
		refresh = str(tokens)
		access = str(tokens.access_token)
		data = {
			"refresh": refresh,
			"access": access
		}
		return data

	def create(self, validated_data):
		user =User(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			
		)
		user.set_password(validated_data['password'])
		user.save()
		client = Client(User = user,phone_no= validated_data['phone_no'])
		client.save()
		return user
