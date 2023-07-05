from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.web_content.models import UTP, About, Delivery, AboutProduction, Product, Contacts


def index(request, *args, **kwargs):
    utp = None
    about = None
    contacts = Contacts.objects.all().first()
    delivery = None
    about_production = None
    products = None
    if request.GET.get('lang'):
        utp = UTP.objects.language(request.GET['lang']).first()
        about = About.objects.language(request.GET['lang']).first()
        delivery = Delivery.objects.language(request.GET['lang']).first()
        about_production = AboutProduction.objects.language(request.GET['lang']).first()
        products = Product.objects.language(request.GET['lang']).all()

    else:
        utp = UTP.objects.language('ru').first()
        about = About.objects.language('ru').first()
        delivery = Delivery.objects.language('ru').first()
        about_production = AboutProduction.objects.language('ru').first()
        products = Product.objects.language('ru').all()
    context = {
        'utp': utp,
        'about': about,
        'delivery': delivery,
        'about_production': about_production,
        'products': products,
    }
    return render(request, 'index.html', context=context)
