from django.contrib import admin
from .models import Agrarprodukte, Nutzflaechen, Nutzflaechenmassnahmen,Produkte,Produktmassnahmen

# Register your models here.
admin.site.register(Agrarprodukte)
admin.site.register(Nutzflaechen)
admin.site.register(Nutzflaechenmassnahmen)
admin.site.register(Produkte)
admin.site.register(Produktmassnahmen)
