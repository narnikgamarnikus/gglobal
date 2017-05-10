# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from gglobal.crm.models import PhoneNumber as Phone
from gglobal.crm.models import MasterCRMProfile, ClientCRMProfile
from cities_light.models import City, Country
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from gglobal.crm.flows import AutoCreateClientFlow
from django.contrib.sites.shortcuts import get_current_site 
from ipware.ip import get_real_ip, get_ip
from geolite2 import geolite2
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site

class UserDetailView(DetailView):
    model = MasterCRMProfile
    template_name = 'users/mastercrmprofile_detail.html'
    # These next two lines tell the view to index lookups by user_id
    slug_field = 'user_id'
    slug_url_kwarg = 'user_id'


class UserRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'user.username': self.request.user.username})


class UserListView(ListView):
    model = MasterCRMProfile
    template_name = 'users/mastercrmprofile_list.html'
    # These next two lines tell the view to index lookups by user_id
    slug_field = 'user_id'
    slug_url_kwarg = 'user_id'
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return context


class UserCityListView(ListView):
    model = City
    template_name = 'users/city_list.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'
    paginate_by = 10

    def get_queryset(self):
        queryset = City.objects.filter(mastercrmprofile__isnull=False).annotate(masters_count=Count('mastercrmprofile')).distinct().order_by('-population').all()
        return queryset


class UserCityDetailView(DetailView):
    model = City
    template_name = 'users/city_detail.html'
    #template_name = 'users/city_list.html'
    slug_field = 'alternate_names'
    slug_url_kwarg = 'alternate_names'

    def get_object(self):
        city = get_object_or_404(City, alternate_names__iexact=self.kwargs['alternate_names'])
        return city

    def get_context_data(self, *args, **kwargs):
        context = super(UserCityDetailView, self).get_context_data(*args, **kwargs)
        context['masters'] = MasterCRMProfile.objects.filter(city__alternate_names=self.kwargs['alternate_names']).order_by('-raiting').all()
        return context

    #def get_queryset(self):
    #    queryset = MasterCRMProfile.objects.filter(city=self.kwargs['alternate_names'])
    #    print(queryset)
    #    return queryset

@csrf_exempt
def СreateClientView(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            ip = get_real_ip(request)
            reader = geolite2.reader()
            data = {
                "form_name"     :   request.POST.get('name'), 
                "phone_number"  :   request.POST.get('phone'),
                "creation_form" :   request.POST.get('form'),
            }
            phone, create = Phone.objects.get_or_create(phone_number=request.POST.get('phone'))
            site = get_current_site(request)
            if ip is not None:
                CityByIP = reader.get(ip)['city']['names']['en']
                CountryByIP = reader.get(ip)['country']['names']['en']
            else:
                ip = get_ip(request)
                if ip is not None:
                    try:
                        CityByIP = reader.get(ip)['city']['names']['en']
                        CountryByIP = reader.get(ip)['country']['names']['en']
                    except:
                        CityByIP = None
                        CountryByIP = None
            if CityByIP and CountryByIP is not None:
                try:
                    city = City.objects.get(name=CityByIP)
                    country = Country.objects.get(name=CountryByIP)
                    AutoCreateClientFlow.start.run(
                        data=data,
                        site=site,
                        city=city,
                        country=country,
                        )
                except ObjectDoesNotExist:
                    pass
            AutoCreateClientFlow.start.run(
                data=data,
                site=site,
                )
            #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
    #Get goes here
    return render(request,'base.html')
