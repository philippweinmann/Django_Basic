from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Sentence(models.Model):
    """Testing Generic Relations"""
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="content_type_sentence")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    sentence = GenericRelation(Sentence)


class Statement(models.Model):
    statement_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    sentence = GenericRelation(Sentence)
