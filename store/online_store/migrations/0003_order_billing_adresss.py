# Generated by Django 2.2 on 2020-10-25 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_billingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_adresss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='online_store.BillingAddress'),
        ),
    ]