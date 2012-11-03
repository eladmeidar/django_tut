from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=90)

class User(models.Model):
  username = models.CharField(max_length=90)
  status = models.CharField(max_length=20)

class Suggestion(models.Model):
  content = models.CharField(max_length=160)
  status = models.CharField(max_length=20)
  created_at = models.DateTimeField('date published')
  category = models.ForeignKey(Category)
  user = models.ForeignKey(User)

  def __unicode__(self):
        return self.content
