#from __future__ import absolute_import
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        # main URLS
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
	# Speech Recognizer URLS
	url(r'^speech_recorder/$', views.speech_recorder, name='speech_recorder'),
	url(r'^cgi_script/$', views.cgi_script, name='cgi_script'),
	# Test URL
	url(r'^test/$', views.test, name='test'),
        # course / lab URLS
        url(r'^course/(?P<course_name_url>\w+)/$', views.course, name='course'),
        url(r'^course/(?P<course_name_url>\w+)/prereq/(?P<prereq_name_url>\w+)/$', views.prereq, name='prereq'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/$', views.lab, name='lab'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/theory/(?P<theory_name_url>\w+)/$', views.theory, name='theory'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/theorytest/(?P<theorytest_name_url>\w+)/$', views.theorytest, name='theorytest'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/simulation/(?P<simulation_name_url>\w+)/$', views.simulation, name='simulation'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/simulationtest/(?P<simulationtest_name_url>\w+)/$', views.simulationtest, name='simulationtest'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/hardware/(?P<hardware_name_url>\w+)/$', views.hardware, name='hardware'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/results/(?P<results_name_url>\w+)/$', views.results, name='results'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/labtest/(?P<labtest_name_url>\w+)/$', views.labtest, name='labtest'),
        # Hardware Help URL
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/hardware/(?P<hardware_name_url>\w+)/hardware_help$', views.hardware_help, name='hardware_help'))

