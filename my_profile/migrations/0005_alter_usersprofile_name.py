# Generated by Django 3.2 on 2022-06-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0004_usersprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]