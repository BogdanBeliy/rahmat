from django.db import models
from parler.managers import TranslatableManager
from parler.models import TranslatedFields, TranslatableModel


class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='back', null=True)


class UTP(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=500, default=""),
        btn_text=models.CharField(max_length=255, default='Продукция')
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
    image = models.ImageField(upload_to='images')


class ShortDescription(TranslatableModel):
    translations = TranslatedFields(
        text=models.CharField(max_length=255)
    )


class Contacts(TranslatableModel):
    translations = TranslatedFields(
        address=models.CharField(max_length=600),
    )
    email = models.EmailField()
    fax = models.CharField(max_length=255)


class Phone(models.Model):
    number = models.CharField(max_length=255)


class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class AcceptionGranulsHeader(TranslatableModel):
    translations = TranslatedFields(
        header=models.CharField(max_length=255)
    )


class AcceptGranulsItem(TranslatableModel):
    translations = TranslatedFields(
        text=models.CharField(max_length=600)
    )


class Requisites(TranslatableModel):
    translations = TranslatedFields(
        fax=models.CharField(max_length=255, default=''),
        rs=models.CharField(max_length=255, default=''),
        address=models.CharField(max_length=600, default=''),
        bank=models.CharField(max_length=600, default=''),
        unn=models.CharField(max_length=255, default=''),
        email=models.CharField(max_length=255, default=''),
    )
