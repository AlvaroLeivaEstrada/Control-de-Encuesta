
# Django rest framework
from rest_framework import serializers


# Models
from surveys.models.survey import Survey


class SurveyModelSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Survey
		fields = (
			'title',
			'about'
		)
  
  
class SurveySerializer(serializers.Serializer):
	
 	title = serializers.CharField()
 	about = serializers.CharField()

 	def validate(self, data):
 		return data

 	def create(self, data):
 		return data


class QuestionSerializer(serializers.Serializer):

	question_text = serializers.CharField(max_length=50)

	def create(self, data):
		return data
