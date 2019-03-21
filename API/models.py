from django.db import models

# Create your models here.
class Produktpass(models.Model):
   agrarprodukt = models.CharField(max_length=50)
   los_chargen = models.CharField(max_length=50)
   longitude = models.FloatField()
   latitude = models.FloatField()
   nutzflächennr = models.CharField(max_length=50)
   massnahmen = models.ManyToManyField('Massnahmen', blank=True)

   def __str__(self):
       return self.agrarprodukt

class Massnahmen(models.Model):
    datum = models.DateTimeField(auto_now=True)
    bearbeitung = models.CharField(max_length=50)


    def __str__(self):
        return self.bearbeitung
