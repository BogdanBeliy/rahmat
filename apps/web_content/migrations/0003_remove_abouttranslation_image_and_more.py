# Generated by Django 4.2.1 on 2023-06-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_content', '0002_alter_abouttranslation_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abouttranslation',
            name='image',
        ),
        migrations.AddField(
            model_name='abouttranslation',
            name='header',
            field=models.CharField(default='Header', max_length=255),
        ),
    ]
