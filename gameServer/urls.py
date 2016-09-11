"""gameServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from server import views
from . import settings

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/$', views.api_test),
	url(r'^api/(?P<gameURL>.+)/(?P<secret>.+)/game$', views.api_getGame, name='api-getgame'),
	url(r'^api/(?P<gameURL>.+)/(?P<secret>.+)/join$', views.api_join, name='api-join'),
	url(r'^api/(?P<gameURL>.+)/(?P<secret>.+)/reconnect$', views.api_reconnect, name='api-reconnect'),
	url(r'^api/(?P<gameURL>.+)/(?P<secret>.+)/numPlayers$', views.api_numPlayers, name='api-numPlayers'),
	url(r'^api/(?P<gameURL>.+)/(?P<secret>.+)/updatePlayer$', views.api_updatePlayer, name='api-updatePlayer'),
	url(r'^api/(?P<gameURL>.+)/(?P<secret>.+)/players$', views.api_getPlayers, name='api-getPlayers'),
	url(r'^(?P<gameURL>.+)$', views.game, name='game'),
	url(r'^$', views.index, name='index')
]
