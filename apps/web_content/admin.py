from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.web_content.models import UTP, About


@admin.register(UTP)
class UTPAdmin(TranslatableAdmin):
    fields = ['title']


@admin.register(About)
class UTPAdmin(TranslatableAdmin):
    fields = ['text']
