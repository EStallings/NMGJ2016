from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from datetime import timedelta
from models import Game, Player, Drawing
from utils.namegen import generate_random_name
from django.forms.models import model_to_dict


# Create your views here.
def index (request):
	print("fuck this general shit")

	name = generate_random_name(split=0)
	secret = generate_random_name(split=2, length=8)
	game = Game.objects.get_or_create(name=name, turn_time=timedelta(minutes=1), secret=secret)
	return HttpResponseRedirect('/' + name)

def game (request, gameURL):
	print("fuck this specific shit")

	try:
		game = Game.objects.get(name=gameURL)
		context = {
			'game_info': game.serializedUnsafe(),
		}
		return render(request, 'server/index.html', context)
	except Game.DoesNotExist:
		return HttpResponseRedirect('/')


def api_getGame (request, gameURL, secret):
	print('getting game data')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret

		return JsonResponse({'game_info' : game.asDict()})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})

def api_numPlayers (request, gameURL, secret):
	print('num players')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret

		return JsonResponse({'numPlayers':game.numPlayers()})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})

def api_getPlayers (reequest, gameURL, secret):
	print('getting players')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret
		players = game.player_set.select_related()
		playerlist = []
		for player in players:
			playerlist += player.asDict()
		return JsonResponse({'players':playerlist})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})

def api_updatePlayer (request, gameURL, secret):
	print('reconnecting to game')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret
		player = Player.objects.get(pk=request.POST['player_pk'])
		assert player.secret == request.POST['player_secret']
		if 'ready' in request.POST:
			player.ready = request.POST['ready']
		if 'name' in request.POST:
			player.name = request.POST['name']
		player.save()
		game.update()
		return JsonResponse({'success' : 'true'})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})


def api_join (request, gameURL, secret):
	print('joining game')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret
		assert game.started == False
		playerDefaultName = 'Player ' + str(int(game.numPlayers()) + 1);
		leader = False
		if(game.numPlayers() == 0):
			leader = True
		player = Player.objects.create(name=playerDefaultName, game=game, secret=generate_random_name(length=6), leader=leader)
	
		return JsonResponse({'player_info' : player.asDictUnsafe()})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})

def api_reconnect(request, gameURL, secret):
	print('reconnecting to game')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret
		player = Player.objects.get(pk=request.POST['player_pk'])
		assert player.secret == request.POST['player_secret']

		return JsonResponse({'player_info' : player.asDictUnsafe()})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})

def api_checkForUpdate(request, gameURL, secret):
	print('checkForUpdate')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret
		player = Player.objects.get(pk=request.POST['player_pk'])
		assert player.secret == request.POST['player_secret']

		return JsonResponse({'player_info' : player.asDictUnsafe()})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})

def api_test (request):
	print('api test')

	return JsonResponse({"FOO BAR FOO":"foobar"})

def api_changeTurnTime (request, gameURL):
	print('reconnecting to game')
	try:
		game = Game.objects.get(name=gameURL)
		assert game.secret == secret
		assert game.started == False

		game.turn_time = datetime.timedelta(seconds=request.POST['seconds'])
		game.save()

		return JsonResponse({'success' : 'true'})
	except Game.DoesNotExist:
		return JsonResponse({'error':'not found', 'response':None})
