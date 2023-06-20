from django.db import models
from parler.managers import TranslatableManager
from parler.models import TranslatedFields, TranslatableModel


class UTP(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=500, default="")
    )
    objects = TranslatableManager()


class About(TranslatableModel):
    translations = TranslatedFields(
        header=models.CharField(max_length=255, default=''),
        text=models.TextField(default=''),
    )


class Delivery(TranslatableModel):
    translation = TranslatedFields(
        header=models.CharField(max_length=255),
        text=models.TextField(default='')
    )


class AboutProduction(TranslatableModel):
    translations = TranslatedFields(
        text=models.TextField(default='')
    )


class Product(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        fraction=models.CharField(max_length=25),
        price=models.CharField(max_length=255),
        additional_information=models.TextField(),
    )


class ShortDescription(models.Model):
    translations = TranslatedFields(
        text=models.CharField(max_length=255)
    )


class Contacts(models.Model):
    address = models.CharField(max_length=600)
    email = models.EmailField()
    fax = models.CharField(max_length=255)


class Phone(models.Model):
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='phones')
