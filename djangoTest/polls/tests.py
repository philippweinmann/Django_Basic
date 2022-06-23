from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from .models import Statement, Sentence


class PollTestCase(TestCase):
    def test_create_statement(self):
        statement = Statement.objects.create(statement_text="example text", pub_date=timezone.now())
        sentence = Sentence.objects.create(content_object=statement)
