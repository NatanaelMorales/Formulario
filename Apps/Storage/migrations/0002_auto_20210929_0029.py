# Generated by Django 2.0.6 on 2021-09-29 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='nombre',
            new_name='nombremasc',
        ),
    ]
