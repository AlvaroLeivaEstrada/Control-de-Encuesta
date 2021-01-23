# Django
from django.db import models

# Models
from surveys.models.survey import Survey




class Question(models.Model):

	question_text = models.CharField(max_length=30, blank=False)
	average = models.PositiveIntegerField(default=0)
	POSSIBLE_ANSWERS = (
		('1', 'very dissatisfied'),
		('2', 'dissatisfied'),
		('3', 'neutral'),
		('4', 'satisfied'),
		('5', 'very satisfied')
	)
	answer = models.CharField(max_length=1, choices=POSSIBLE_ANSWERS)
	survey = models.ForeignKey('Survey', on_delete=models.CASCADE)