import logging
from server.utils.http import JsonView, get, put, delete

from django.conf import settings
log = logging.getLogger(__name__)

class GameView(JsonView):
	
	def get(self, request):
		if not 'HTTP_AUTHORIZATION' in request.META:
			return None, 401

		return get(settings.VIDISPINE_API + 'shape-tag', request.META['HTTP_AUTHORIZATION'], accept='application/json'), 200