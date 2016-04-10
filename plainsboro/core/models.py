from django.db import models
from django.shortcuts import resolve_url as r


class Doctor(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    address = models.CharField('endereço', max_length=255)
    neighborhood = models.CharField('bairro', max_length=255)
    city = models.CharField('cidade', max_length=255)
    phone = models.CharField('telefone', max_length=255)
    email = models.CharField('email', max_length=255)
    specialization = models.CharField('especialização', max_length=255)

    class Meta():
        verbose_name = 'médico'
        verbose_name_plural = 'médicos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('doctor_details', slug=self.slug)
