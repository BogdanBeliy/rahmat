from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.web_content.forms import LeadForm
from apps.web_content.models import UTP, About, Delivery, AboutProduction, Product, Contacts, ShortDescription, Phone, \
    AcceptionGranulsHeader, AcceptGranulsItem


def index(request, *args, **kwargs):
    utp = None
    about = None
    contacts = None
    phones = Phone.objects.all()
    delivery = None
    about_production = None
    products = None
    short_description = None
    accept_granuls_header = None
    accept_granuls_items = None

    if request.GET.get('lang'):
        utp = UTP.objects.language(request.GET['lang']).first()
        about = About.objects.language(request.GET['lang']).first()
        delivery = Delivery.objects.language(request.GET['lang']).first()
        about_production = AboutProduction.objects.language(request.GET['lang']).first()
        products = Product.objects.language(request.GET['lang']).all()
        short_description = ShortDescription.objects.language(request.GET['lang']).first()
        contacts = Contacts.objects.language(request.GET['lang']).first()
        accept_granuls_header = AcceptionGranulsHeader.objects.language(request.GET['lang']).first()
        accept_granuls_items = AcceptGranulsItem.objects.language(request.GET['lang']).all()
    else:
        utp = UTP.objects.language('ru').first()
        about = About.objects.language('ru').first()
        delivery = Delivery.objects.language('ru').first()
        about_production = AboutProduction.objects.language('ru').first()
        products = Product.objects.language('ru').all()
        short_description = ShortDescription.objects.language('ru').first()
        contacts = Contacts.objects.language('ru').first()
        accept_granuls_header = AcceptionGranulsHeader.objects.language('ru').first()
        accept_granuls_items = AcceptGranulsItem.objects.language('ru').all()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'utp': utp,
        'about': about,
        'delivery': delivery,
        'about_production': about_production,
        'products': products,
        'short_description': short_description,
        "phones": phones,
        'contacts': contacts,
        'accept_granuls_header': accept_granuls_header,
        'accept_granuls_items': accept_granuls_items,
        'form': LeadForm()
    }
    return render(request, 'index.html', context=context)
