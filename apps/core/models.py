import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_integer
from django.db import models


class GeneralInformation(models.Model):
    datetime = models.DateTimeField('Fecha y hora')
    location = models.TextField('Lugar')
    description = models.TextField('Descripción')

    # banner (foto 16:9)

    def __str__(self):
        return 'Información general del Marabana'


class TitleTextBaseModel(models.Model):
    title = models.CharField('Título', max_length=100)
    text = models.TextField('Texto', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class ExtraInformation(TitleTextBaseModel):
    location = models.CharField('Ubicación', max_length=300)
    start_date = models.DateTimeField('Fecha inicio')
    end_date = models.DateTimeField('Fecha fin')
    photo = models.ImageField('Foto', upload_to='images/', null=True, blank=True)


class Category(TitleTextBaseModel):
    pass


class Rule(TitleTextBaseModel):
    pass


categories = (
    ('m', 'Maratón'),
    ('mm', 'Media Maratón'),
    ('10', '10 km'),
    ('msr', 'Maratón silla de ruedas'),
    ('mmsr', 'Medio Maratón silla de ruedas'),
    ('10sr', '10 km silla de ruedas'),
)


class Result(models.Model):
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellidos', max_length=200)
    country = models.CharField('País', max_length=100)
    gender = models.SmallIntegerField('Género', choices=(
        (0, 'M'),
        (1, 'F')
    ))
    email = models.EmailField('Correo')
    duration = models.PositiveIntegerField('Duración en minutos')
    date = models.DateField('Fecha de de la carrera', default=datetime.datetime.utcnow())
    category = models.CharField('Categoría', max_length=10, choices=categories)

    def __str__(self):
        return f'Resultado de carrera de {self.name} {self.last_name}'


class Inscription(models.Model):
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellidos', max_length=200)
    address = models.TextField('Dirección')
    country = models.CharField('País', max_length=100)
    postal_code = models.CharField('Código postal', max_length=5, validators=[MinLengthValidator(5), validate_integer])
    dni = models.CharField('Carnet de id', max_length=11, validators=[MinLengthValidator(11), validate_integer])
    birth_date = models.DateField('Fecha de nacimiento')
    gender = models.SmallIntegerField('Género', choices=(
        (0, 'Masculino'),
        (1, 'Femenino')
    ))
    phone = models.CharField('Teléfono', max_length=8, validators=[MinLengthValidator(8), validate_integer])
    email = models.EmailField('Correo')
    email_confirm = models.EmailField('Confirmación de correo')
    average_time = models.PositiveSmallIntegerField('Tiempo estimado', choices=(
        (1, 'Menos de 3h'),
        (2, 'Entre 3h y 3h15'),
        (3, 'Entre 3h15 y 3h30'),
        (4, 'Entre 3h30 y 3h45'),
        (5, 'Entre 3h45 y 4h'),
        (6, 'Más de 4h'),
    ))
    race_rules = models.BooleanField('Reglamento de la carrera', default=False)
    is_active = models.BooleanField('Aprobada', default=False)

    def clean(self):
        if self.email != self.email_confirm:
            raise ValidationError({'email_confirm': 'Los correos no coinciden.'})
        if self.race_rules is False:
            raise ValidationError({'race_rules': 'Debe estar de acuerdo con el reglamento de la carrera.'})
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save()

    def __str__(self):
        return f'Inscripción de {self.name} {self.last_name}'


class Fotografia(models.Model):
    image = models.ImageField('Imagen', upload_to='images/')

    def __str__(self):
        return self.image.name


class Notice(TitleTextBaseModel):
    date = models.DateTimeField('Fecha')
    image = models.ImageField('Imagen', upload_to='images/')


class Contact(models.Model):
    type = models.CharField('Tipo de contacto', max_length=120)
    name = models.CharField('Nombre', max_length=120)
    address = models.TextField('Dirección')
    phone = models.CharField('Teléfono', max_length=8, validators=[validate_integer])
    email = models.EmailField('Correo')
    web = models.URLField('Sitio Web')
