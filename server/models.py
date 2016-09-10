from __future__ import unicode_literals
from django.core import serializers
from django.db import models
from django.db.models.fields.files import ImageField
import simplejson


# Create your models here.
class Game(models.Model):
	name         = models.CharField(max_length=200)
	secret       = models.CharField(max_length=200)
	created_date = models.DateTimeField(auto_now=True)
	turn_time    = models.DurationField()
	started      = models.BooleanField(default=False)
	turnNumber   = models.IntegerField(default = 0)

	def numPlayers(self):
		return self.player_set.select_related().count();

	def numPlayersReady(self):
		return self.player_set.select_related(ready=True).count();

	def serializedUnsafe(self): #all fields including secret
		return serializers.serialize('json', [self])

	def serialized(self): #everything but the secret
		return serializers.serialize('json', [self], fields={'name', 'created_date', 'turn_time', 'started'})

	def asDict(self):
		return simplejson.loads(self.serialized())

	def asDictUnsafe(self):
		return simplejson.loads(self.serializedUnsafe())

class Player(models.Model):
	game   = models.ForeignKey(Game, on_delete=models.CASCADE)
	name   = models.CharField(max_length=200)
	secret = models.CharField(max_length=200)
	ready  = models.BooleanField(default=False)

	def serializedUnsafe(self): #all fields including secret
		return serializers.serialize('json', [self])

	def serialized(self): #everything but the secret
		return serializers.serialize('json', [self], fields={'name', 'ready'})

	def asDict(self):
		return simplejson.loads(self.serialized())

	def asDictUnsafe(self):
		return simplejson.loads(self.serializedUnsafe())

class Drawing(models.Model):
	game           = models.ForeignKey(Game, on_delete=models.CASCADE)
	number         = models.IntegerField(default=0)
	player         = models.ForeignKey(Player, related_name='player')
	startingPlayer = models.ForeignKey(Player, related_name='startingPlayer')
	caption        = models.CharField(max_length=200)
	file           = models.FileField()



# class Game(models.Model):

# class Game(models.Model):


