from django.conf.urls import url

from . import views

app_name = 'laddr'
urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'^home/$', views.home_page, name='home'),
    url(r'^teams/$', views.teams_page, name='teams'),
    url(r'^compete/$', views.compete_page, name='compete'),
    url(r'^profile/$', views.profile_page, name='profile'),
    url(r'^store/$', views.store_page, name='store'),
    url(r'^find_team/$', views.find_team, name='find_team'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^events/$', views.events, name='events'),
    url(r'^patch_notes/$', views.patch_notes, name='patch_notes'),
    url(r'^login/$', views.login_page, name='login'),
]