from django.urls import path
from rest_framework.routers import DefaultRouter

from .question_api import QuestionViewSet
from .sentence_api import SentenceViewSet
from .statement_api import StatementViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'statements', StatementViewSet, basename='statements')
router.register(r'sentences', SentenceViewSet, basename='sentences')

urlpatterns = router.urls
