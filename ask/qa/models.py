from django.contrib.auth.models import User
from django.db import models


# Create your models here

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=256)
    text = models.TextField(default='')
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='authors_questions')
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def get_absolute_url(self):
        return '/question/%i/' % self.id


class Answer(models.Model):
    objects = models.Manager()
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
