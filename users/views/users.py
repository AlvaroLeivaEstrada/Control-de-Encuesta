# Django Rest Framework
from rest_framework import status,viewsets,mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# Serializer
from users.serializers.users import (
	UserSerializer,
	UserLoginSerializer,
	UserSignUpSerializer
)


# Models
from users.models.users import User


class UserViewSet(
				viewsets.GenericViewSet,
				mixins.ListModelMixin):
	"""User view Set """

	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_permissions(self):

		if self.action in ['login', 'signup','allusers']:
			permissions = [AllowAny]
		elif self.action in ['update', 'delete']:
			permissions=[IsAuthenticated]
		else:
			permissions = [IsAuthenticated]
		return [p() for p in permissions]


	@action(detail=False, methods=['post'])
	def signup(self, request):
		serializer = UserSignUpSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		data = UserSerializer(user).data
		return Response(data, status=status.HTTP_201_CREATED)


	@action(detail=False, methods=['post'])
	def login(self, request):
		serializer = UserLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, token = serializer.save()
		data = {
			'user': UserSerializer(user).data,
			'access_token': token
		}
		return Response(data, status=status.HTTP_201_CREATED)

		
	@action(detail=False, methods=['get'])
	def allusers(self, request):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)

