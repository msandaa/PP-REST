from django.contrib import admin
from .models import Agrarprodukt, Anbau, Anbaumassnahmen

# Register your models here.
admin.site.register(Agrarprodukt)
admin.site.register(Anbau)
admin.site.register(Anbaumassnahmen)
