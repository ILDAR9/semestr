# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    url(r'^thanks$', direct_to_template, {'template': '404.html'}),
    url(r'^test', 'semestr.views.contact'),
#    url(r'^start_programm$', direct_to_template, {'template' : 'preview.html'}),
    url(r'^execute$', 'semestr.views.execute'),
    url(r'^document$', 'semestr.views.download_file'),
    url(r'^decode$',direct_to_template, {'template':'decode.html'}),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
{'document_root': settings.STATIC_ROOT}),
        (r'^media/static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT  }),
        
    )