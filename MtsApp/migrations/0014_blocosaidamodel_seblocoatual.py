# Generated by Django 3.0.8 on 2020-08-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MtsApp', '0013_auto_20200801_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocosaidamodel',
            name='SeBlocoAtual',
            field=models.TextField(blank=True, default='', max_length=3),
        ),
    ]
