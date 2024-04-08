from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class MenuView(TemplateView):
    template_name = 'menu_page.html'

    def get_context_data(self, slug, **kwargs):
        return {'menu_name': slug}
