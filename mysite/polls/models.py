from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_topic = models.CharField(max_length=30)
    pub_date = models.DateTimeField("date publised")

    # Whenever we query the question
    # it will be represented by what the question is
    # instead of its id
    def __str__(self):
        return self.question_text
    
    # changes how the admin views it.
    # must be imedietely above was_published_recently to work!!!
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
