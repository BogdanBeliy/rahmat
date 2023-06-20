from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.web_content.models import UTP


class ContentView(ListView):
    template_name = 'index.html'
    queryset = UTP.objects.all()
    context_object_name = 'utp'

    def get(self, request, *args, **kwargs):
        if request.GET.get('lang'):
            self.object_list = self.queryset.language(request.GET['lang']).first()
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            self.object_list = self.queryset.language('ru').first()
            context = self.get_context_data()
            return self.render_to_response(context)
