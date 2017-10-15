# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class TiposDeServicio(models.Model):
    nombre = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='services')

    def __unicode__(self):
        return u'{0}'.format(self.nombre)


class Trabajador(models.Model):
    nombre = models.CharField(max_length=1000)
    apellidos = models.CharField(max_length=1000)
    aniosExperiencia = models.IntegerField()
    tiposDeServicio = models.ForeignKey(TiposDeServicio, null=True)
    telefono = models.CharField(max_length=1000)
    correo = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='photos')
    usuarioId = models.OneToOneField(User, null=True)


class Comentario(models.Model):
    texto = models.CharField(max_length=1000)
    trabajador = models.ForeignKey(Trabajador, null=True)
    correo = models.CharField(max_length=1000)
