# Generated by Django 2.2 on 2020-10-26 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0006_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]