# Generated by Django 4.1.3 on 2022-12-22 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='school',
            new_name='name',
        ),
    ]