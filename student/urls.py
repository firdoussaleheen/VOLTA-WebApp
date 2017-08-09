from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_change, password_change_done
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/(?P<user_name_url>\w+)/$', views.profile, name='profile'),
    url(r'^change-password/$', 'django.contrib.auth.views.password_change'),
    url(r'^change/$', password_change, {'template_name': 'VLA/password_change_form.html'}, name='password_change'),
    url(r'^change-done/$', password_change_done, {'template_name': 'VLA/password_change_done.html'}, name='password_change_done'),
)
