from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __init__(self,question_text,pub_date):
        return self.question_text

class Choices(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __init__(self,choice_text,question,votes):
        return self.choice_text
# Create your models here.
