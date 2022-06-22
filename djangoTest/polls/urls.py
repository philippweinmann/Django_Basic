from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .question_api import QuestionViewSet
from .statement_api import StatementViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'statements', StatementViewSet, basename='statements')

urlpatterns = router.urls
