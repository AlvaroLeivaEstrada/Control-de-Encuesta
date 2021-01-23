# Django
from django.contrib.auth import authenticate, password_validation
#Models
from users.models.users import User

# Serializer
from surveys.serializers.surveys import SurveyModelSerializer

# Django rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
	
	created_survey = SurveyModelSerializer(read_only=True)
	class Meta:
		model = User
		fields = (
			'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'created_survey'
        )

class UserLoginSerializer(serializers.Serializer):


	email = serializers.EmailField()
	password = serializers.CharField(min_length=3,max_length=84)

	def validate(self, data):

		user = authenticate(username=data['email'], password=data['password'])
		if not user:
			raise serializers.ValidationError('Invalid credentials')
		self.context['user'] = user
		return data

	def create(self, data):
		token, created = Token.objects.get_or_create(user=self.context['user'])
		return self.context['user'], token.key

class UserSignUpSerializer(serializers.Serializer):

	email = serializers.EmailField(
		validators=[UniqueValidator(queryset=User.objects.all())]
	)
	username = serializers.CharField(
		min_length=4,
		max_length=20,
		validators=[UniqueValidator(queryset=User.objects.all())]
	)


	password = serializers.CharField(min_length=8, max_length=64)
	password_confirmation = serializers.CharField(min_length=8,max_length=64)


	first_name = serializers.CharField(min_length=2,max_length=30)
	last_name = serializers.CharField(min_length=2,max_length=30)

	def validate(self, data):
		password = data['password']
		password_conf = data['password_confirmation']
		if password != password_conf:
			raise serializers.ValidationError('Password does not match')
		password_validation.validate_password(password)
		return data
	def create(serlf, data):
		data.pop('password_confirmation')
		return User.objects.create_user(**data)

