from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Statement(models.Model):
    statement_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
