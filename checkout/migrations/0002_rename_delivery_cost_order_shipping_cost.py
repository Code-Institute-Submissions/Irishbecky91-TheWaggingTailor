# Generated by Django 3.2 on 2022-06-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_cost',
            new_name='shipping_cost',
        ),
    ]
