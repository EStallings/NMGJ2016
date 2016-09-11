from __future__ import unicode_literals
from django.core import serializers
from django.db import models
from django.db.models.fields.files import ImageField
import simplejson
import datetime
from django.utils import timezone

def cleanupOldGames():
	games = Game.objects.get(updated__lte=timezone.now() - datetime.timedelta(days=1))
	for game in games:
		game.delete()

# Create your models here.
class Game(models.Model):
	name         = models.CharField(max_length=200)
	secret       = models.CharField(max_length=200)
	created_date = models.DateTimeField(auto_now=True)
	turn_time    = models.DurationField()
	started      = models.BooleanField(default=False)
	turnNumber   = models.IntegerField(default = 0)
	updated      = models.DateTimeField(default = datetime.datetime.now())

	def numPlayers(self):
		return self.player_set.select_related().count();

	def numPlayersReady(self):
		return self.player_set.select_related().filter(ready=True).count();

	def serializedUnsafe(self): #all fields including secret
		return serializers.serialize('json', [self])

	def serialized(self): #everything but the secret
		return serializers.serialize('json', [self], fields={'name', 'created_date', 'turn_time', 'started'})

	def asDict(self):
		return simplejson.loads(self.serialized())

	def asDictUnsafe(self):
		return simplejson.loads(self.serializedUnsafe())

	def update(self):
		print('updating game')
		if(not self.started):
			print('have not started')
			# for player in self.player_set.select_related().filter(ready=False):
			# 	print ('player ' + player.name + ' not ready')
			# 	if(player.active + datetime.timedelta(seconds=3) < timezone.now()):
			# 		print ('player ' + player.name + ' being kicked as inactive')
			# 		player.delete()
			if(self.numPlayers() == self.numPlayersReady()):
				self.started = True
		
		self.updated = datetime.datetime.now()
		self.save()

class Player(models.Model):
	game   = models.ForeignKey(Game, on_delete=models.CASCADE)
	name   = models.CharField(max_length=200)
	secret = models.CharField(max_length=200)
	ready  = models.BooleanField(default=False)
	active = models.DateTimeField(default=datetime.datetime.now())
	leader = models.BooleanField(default=False)

	def outdated(self):
		return game.updated > self.active

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


