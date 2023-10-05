from django.db import models


# Create your models here.

class GeneralInformation(models.Model):
    # fecha y hora
    # lugar
    # description
    # banner (foto 16:9)

    pass


class ExtraInformation(models.Model):
    # ubicacion
    # fecha inicio
    # Fecha fin
    # hora inicio
    # hora fin
    # foto
    pass


class GeneralInformationCategory(models.Model):
    # title
    # text ( optional)
    pass


class Rule(models.Model):
    # title
    # text
    pass


class Campeonato(models.Model):
    # title
    # text
    pass


class Inscription(models.Model):
    # banner
    # nombre
    # apellidos
    # Direccion
    # Pais
    # codigo postal
    # DNI
    # fecha de nacimiento
    # Genero M o F
    # telefono
    # email
    # email confirmation
    # tiempo estimado en horas
    pass


class Fotografia(models.Model):
    # image field
    pass


class Notice(models.Model):
    # title
    # Text
    # date
    # image
    pass


class Contact(models.Model):
    # type
    # name
    # address
    # tel
    # email
    # web
    pass