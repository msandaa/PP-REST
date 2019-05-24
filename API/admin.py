from django.contrib import admin
from .models import Agrarprodukte, Nutzflaechen, Nutzflaechenmassnahmen,Produkt,Produktmassnahmen

# Register your models here.
admin.site.register(Agrarprodukte)
admin.site.register(Nutzflaechen)
admin.site.register(Nutzflaechenmassnahmen)
admin.site.register(Produkt)
admin.site.register(Produktmassnahmen)
