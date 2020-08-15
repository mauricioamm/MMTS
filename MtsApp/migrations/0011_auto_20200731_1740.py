# Generated by Django 3.0.8 on 2020-07-31 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MtsApp', '0010_blocosaidamodel_errotipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedcond1model',
            name='CriterioErrosTipo',
            field=models.TextField(blank=True, default='', max_length=5),
        ),
        migrations.AddField(
            model_name='procedcond1model',
            name='CriterioTotal',
            field=models.TextField(blank=True, default='', max_length=5),
        ),
        migrations.AddField(
            model_name='procedcond2model',
            name='CriterioErrosTipo',
            field=models.TextField(blank=True, default='', max_length=5),
        ),
        migrations.AddField(
            model_name='procedcond2model',
            name='CriterioTotal',
            field=models.TextField(blank=True, default='', max_length=5),
        ),
    ]
