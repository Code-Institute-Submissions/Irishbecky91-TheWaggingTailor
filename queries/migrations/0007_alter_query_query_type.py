# Generated by Django 3.2 on 2022-06-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0006_alter_query_query_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_type',
            field=models.CharField(choices=[('QUOTE', 'Request A Quote'), ('QUERY', 'Ask A Question')], max_length=20),
        ),
    ]
