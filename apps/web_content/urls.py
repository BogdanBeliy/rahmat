from django.urls import path

from apps.web_content.views import ContentView

urlpatterns = [
    path('', ContentView.as_view()),
]

