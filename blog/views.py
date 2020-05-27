from django.shortcuts import render
from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['message'] = 'Hello World!'
        return context
