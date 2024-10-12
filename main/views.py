from django.shortcuts import render
from django.views.generic import TemplateView

class BasePageView(TemplateView):
    template_name = 'main/base.html'  #

class HomePageView(TemplateView):
    template_name = 'main/home.html'

class AboutPageView(TemplateView):
    template_name = 'main/about.html'
