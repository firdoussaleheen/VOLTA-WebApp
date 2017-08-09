from __future__ import absolute_import
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        # main URLS
        url(r'^$', views.help, name='help'),
        url(r'^vocabtopic/(?P<vocab_topic_name_url>\w+)/$', views.vocab_topic, name='vocab_topic'),
        url(r'^questiontopic/(?P<question_topic_name_url>\w+)/$', views.question_topic, name='question_topic'),
        url(r'^definition/(?P<definition_name_url>\w+)/$', views.definition, name='definition'),
        url(r'^question/(?P<question_name_url>\w+)/$', views.question, name='question'),
        url(r'^suggest_definition/$', views.suggest_definition, name='suggest_definition'),
        url(r'^suggest_question/$', views.suggest_question, name='suggest_question'),
        
        )