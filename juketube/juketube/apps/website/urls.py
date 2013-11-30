from django.conf.urls import patterns, url
import views
#from juketube.apps.website.views import index

urlpatterns = patterns("",
    url(r"^$", views.index, name="index"),
    url(r'^search/$', views.search, name='search'),
    url(r'^updatePlaylist/$', views.updatePlaylist, name='updatePlaylist'),
    url(r'^getUpdatedPlaylist/$', views.getUpdatedPlaylist, name='getUpdatedPlaylist'),
    url(r'^create/$', views.shared_create, name='create'),
    url(r'^playlists/(?P<playlist_slug>[\+\w\.@-_]+)/$', views.shared_list, name='shared_list'),
    
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^node_api$', views.node_api, name='node_api'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)