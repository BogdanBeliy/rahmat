from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.web_content.models import UTP, About, Delivery, Product, Contacts


@admin.register(UTP)
class UTPAdmin(TranslatableAdmin):
    fields = ['title', 'btn_text']


@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    fields = ['text', 'header']


@admin.register(Delivery)
class DeliveryAdmin(TranslatableAdmin):
    fields = ['header', 'text']


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    fields = ['title', 'fraction', 'price', 'additional_information', 'image']


@admin.register(Contacts)
class DeliveryAdmin(TranslatableAdmin):
    fields = ['address', 'fax', 'email']
