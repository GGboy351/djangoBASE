from django.shortcuts import render
from django.views.generic import TemplateView

class mainPAGE(TemplateView):
    template_name = "home.html"

class test(TemplateView):
    template_name = "test.html"