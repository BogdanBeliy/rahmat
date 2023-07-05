from django.urls import path

from apps.web_content.views import index

urlpatterns = [
    path('', index),
]

