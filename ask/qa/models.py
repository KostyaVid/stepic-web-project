from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
   def new(self):
      return self.order_by('-id')
   def popular(self):
      return self.order_by('-rating')


class Question(models.Model):
   title = models.CharField(max_length=250)
   text = models.TextField()
   added_at = models.DateField(auto_now_add=True)
   rating = models.IntegerField(default=0)
   author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
   likes = models.ManyToManyField(User, blank=True, related_name='question_like_user')
   objects = QuestionManager()

   def get_url(self):
      return reverse('question', args=(self.id,))


class Answer(models.Model):
   text = models.TextField()
   added_at = models.DateField(auto_now_add=True)
   question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
   author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)