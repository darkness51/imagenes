from django.conf.urls import patterns, url


urlpatterns = patterns('subir.views',
	url(r'^foto$', 'foto_vista', name='home'),
)