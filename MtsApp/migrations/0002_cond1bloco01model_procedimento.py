# Generated by Django 3.0.8 on 2020-07-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MtsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cond1bloco01model',
            name='Procedimento',
            field=models.TextField(blank=True, default='', max_length=50),
        ),
    ]
