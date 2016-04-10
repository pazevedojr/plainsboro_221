# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('address', models.CharField(max_length=255, verbose_name='endereço')),
                ('neighborhood', models.CharField(max_length=255, verbose_name='bairro')),
                ('city', models.CharField(max_length=255, verbose_name='cidade')),
                ('phone', models.CharField(max_length=255, verbose_name='telefone')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('specialization', models.CharField(max_length=255, verbose_name='especialização')),
            ],
            options={
                'verbose_name_plural': 'médicos',
                'verbose_name': 'médico',
            },
        ),
    ]
