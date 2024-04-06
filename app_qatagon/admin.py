from django.contrib import admin

# Register your models here.

from app_qatagon.models import Event, AffectedIndividual

admin.site.register(Event)
admin.site.register(AffectedIndividual)