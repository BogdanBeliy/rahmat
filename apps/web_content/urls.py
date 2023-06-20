from django.urls import path

from apps.web_content.views import HeaderContentView

urlpatterns = [
    path('', HeaderContentView.as_view()),
]

