import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)    # Camel Case == that it is a class
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(           # connect this to a question
        Question,
        on_delete=models.CASCADE            # if there's a choice that was referencing a deleted question, also delete the choice/s (?) related 
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


    