# Django rest framework
from rest_framework import status,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny

# Serializer
from surveys.serializers.surveys import(
	SurveySerializer,
	SurveyModelSerializer
) 

# Model
from surveys.models.survey import Survey

class SurveyViewSet(viewsets.GenericViewSet):

	queryset = Survey.objects.all()
	serializer_class = SurveyModelSerializer
	allowed_methods = ['post', 'get']

	def get_permissions(self):
		if self.action in ['newsurvey', 'retrieve']:
			permissions = [AllowAny]
		else:
			permissions = [AllowAny]
		return [p() for p in permissions]

	def retrieve(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = SurveySerializer(queryset, many=True)
		return Response(serializer.data)


	@action(detail=False, methods=['post'])
	def newsurvey(self, request):
		serializer = SurveySerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		survey = serializer.save()
		data = SurveyModelSerializer(survey).data
		return Response(data, status=status.HTTP_201_CREATED)


	
	def addquestion(self, request):
		pass
