from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class Question(models.Model):
    questionText = models.CharField(max_length = 100)
    publishDate = models.DateTimeField('date published')

    def lastSevenDays(self):
        return (self.publishDate >= timezone.now() - datetime.timedelta(days=7)) and (self.publishDate <= timezone.now())

    def lastDay(self):
        return (self.publishDate >= timezone.now() - datetime.timedelta(days=1)) and (self.publishDate <= timezone.now())

    def __str__(self):
        return self.questionText

    lastSevenDays.admin_order_field = publishDate
    lastSevenDays.boolean = True
    lastSevenDays.short_description = 'Last week?'

class Answer(models.Model):
    answerText = models.CharField(max_length = 100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question) #An answer belongs to a question (references the question it answers)

    def __str__(self):
        return self.answerText
