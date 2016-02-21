from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Lab(models.Model):
    labName = models.CharField(max_length=200)
    dateCreated = models.DateTimeField('date published')
	labQuestion = models.CharField(max_length=200)
	def __str__(self):
        return self.labName
    def was_published_recently(self):
        return self.dateCreated >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'dateCreated'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
