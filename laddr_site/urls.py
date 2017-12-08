from django.conf.urls import url

from . import views

app_name = 'laddr'
urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'^home/$', views.home_page, name='home'),
    url(r'^teams/$', views.teams_page, name='teams'),
    url(r'^compete/$', views.compete_page, name='compete'),
    url(r'^profile/$', views.profile_page, name='profile'),
]