from django.db import models
from countries_languages.choices.all_country import COUNTRIES
from countries_languages.choices.all_language import LANGUAGES


class Person(models.Model):
    """Персонал"""
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Отчество', max_length=100)
    birthday = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/', default='no_photo.png', blank=True, null=True)
    country = models.TextField(verbose_name='Старна', choices=COUNTRIES, default='BY')
    language = models.TextField(verbose_name='Язык', choices=LANGUAGES, default='RU')
    organization = models.ForeignKey('Organization', verbose_name='Организация', on_delete=models.RESTRICT)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Organization(models.Model):
    """Организация"""
    name = models.CharField(verbose_name='Организация', max_length=250)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'

    def __str__(self):
        return self.name

