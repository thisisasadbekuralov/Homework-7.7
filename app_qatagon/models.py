from django.db import models

# Create your models here.

from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Hodisa')
    date = models.DateField(verbose_name='Sana')
    description = models.TextField(verbose_name='Tavsifi')
    location = models.CharField(max_length=100, verbose_name='Hodisa sodir etilgan joyi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hodisa'
        verbose_name_plural = 'Hodisalar'
        db_table = 'event'


class AffectedIndividual(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ismi Sharifi', blank=False, null=False)
    data_of_birth = models.DateField(verbose_name='Tugulgan sanasi')
    occupation = models.CharField(max_length=100, verbose_name='Kasbi', blank=True, null=True)
    description = models.TextField(verbose_name='Tavsifi')
    event_person = models.ForeignKey(Event, on_delete=models.CASCADE)
    person_image = models.ImageField(upload_to='static/', blank=True, null=True, verbose_name='Qatag`on qurboni surati')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Qatag`on qurbonlari'
        verbose_name_plural = 'Qatag`on qurbonlari'
        db_table = 'people'
