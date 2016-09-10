from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
	url = models.CharField(max_length=200)
	created_date = models.DateTimeField()
	turn_time = models.DateTimeField()

# class WritingPrompt(models.Model):


# class Drawing(models.Model):

# class Game(models.Model):

# class Game(models.Model):