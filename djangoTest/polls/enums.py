from django.db import models


class SentencesContentTypes(models.TextChoices):
    __order__ = 'QUESTION STATEMENT'
    QUESTION = "question"
    STATEMENT = "statement"
