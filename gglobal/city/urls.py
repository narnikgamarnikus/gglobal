# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views
from django.views.generic

urlpatterns = [
    url(r'^$', generic.TemplateView.as_view(template_name='service/index.html'), name='index'),

    url(
        regex=r'^$',
        view=views.CityListView.as_view(),
        name='cities'
    ),
    url(
        regex=r'^(?P<alternate_names>[\w.@+-]+)$',
        view=views.CityDetailView.as_view(),
        name='city'
    ),
    url(
        regex=r'^(?P<alternate_names>[\w.@+-]+)/(?P<slug>[\w.@+-]+)/$',
        view=views.CityServiceDetailView.as_view(),
        name='city-service'
    ),
    #url(
    #    regex=r'^(?P<alternate_names>[\w.@+-]+)/заказы/$',
    #    view=views.CityProjectsListView.as_view(),
    #    name='city-projects'
    #),
    #url(
    #    regex=r'^(?P<alternate_names>[\w.@+-]+)/заказ/(?P<pk>[\w.@+-]+)$',
    #    view=views.CityProjectDetailView.as_view(),
    #    name='city-project'
    #),
]


#urlpatterns = [
#    url(
#        r'^автокомплит-городов/$',
#        views.CityAutocomplete.as_view(),
#        name='city-autocomplete',
#    ),
#]