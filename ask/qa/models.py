from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
   def new(self):
      return self.order_by('-added_at')
   def popular(self):
      return self.order_by('-rating')


class Question(models.Model):
   title = models.CharField(max_length=250)
   text = models.TextField()
   added_at = models.DateField(auto_now_add=True)
   rating = models.IntegerField(default=0)
   author = models.ForeignKey(User, on_delete=models.SET_NULL)
   likes = models.ManyToManyField(User,related_name='question_like_user')
   questions = QuestionManager()


class Answer(models.Model):
   text = models.TextField()
   added_at = models.DateField(auto_now_add=True)
   questions = models.OneToOneField(Question, on_delete=models.SET_NULL)
   author = models.CharField(max_length=250)

   class Meta:
      ordering = ['-added_at']
