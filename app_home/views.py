from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "home.html"

