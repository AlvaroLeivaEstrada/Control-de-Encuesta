# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import surveys as survey_views

router = DefaultRouter()
router.register(r'surveys', survey_views.SurveyViewSet, 
	basename='surveys'
)

urlpatterns = [
    path('', include(router.urls))
]


# 'users/(?P<username>[-a-zA-Z0-0_]+)'