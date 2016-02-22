from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Lab(models.Model):
    lab_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question = models.CharField(max_length=200)
    def __str__(self):
        return self.lab_name

class Submission(models.Model):
    lab = models.ForeignKey(Lab)
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField(max_length=254)
    input_int = models.IntegerField()
    def __str__(self):
        return self.student_name
