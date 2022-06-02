from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .question_api import QuestionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='questions')

urlpatterns = router.urls
