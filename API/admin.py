from django.contrib import admin
from .models import Agrarprodukt, Anbau, Anbaumassnahmen,Produkt,Produktmassnahmen

# Register your models here.
admin.site.register(Agrarprodukt)
admin.site.register(Anbau)
admin.site.register(Anbaumassnahmen)
admin.site.register(Produkt)
admin.site.register(Produktmassnahmen)
