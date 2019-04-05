from django.db import models

# Create your models here.
class Agrarprodukt(models.Model):

   agrarprodukt = models.CharField(max_length=50)
   los_chargennummer = models.CharField(max_length=50)

   produktionsart = models.CharField(max_length=50)

   def __str__(self):
       return self.agrarprodukt

class Anbau(models.Model):

    verantwortlicher = models.ForeignKey('auth.User', related_name='anbau', on_delete=models.PROTECT)
    agrarprodukt = models.ForeignKey(Agrarprodukt, related_name = 'anbau', on_delete=models.CASCADE)


    nutzflaechennr = models.CharField(max_length=50)
    nutzflaeche = models.CharField(max_length=50)

    #kreisnummer = models.CharField(max_length=50)
    #kreis = models.CharField(max_length=50)
    #bundeslandnummer = models.CharField(max_length=50)
    #bundelsland = models.CharField(max_length=50)


    def __str__(self):
        return self.nutzflaechennr

class Anbaumassnahmen(models.Model):

    verantwortlicher = models.ForeignKey('auth.User', related_name='anbaumassnahmen', on_delete=models.PROTECT)
    anbau = models.ForeignKey(Anbau, related_name='anbaumassnahmen',on_delete=models.CASCADE)

    massnahme = models.CharField(max_length=50)
    landwirtschftliches_nutzfahrzeug = models.CharField(max_length=50)
    startuhrzeit_der_bearbeitung = models.CharField(max_length=50)

    #datum = models.DateTimeField()
    #enduhrzeit_der_bearbeitung = models.CharField(max_length=50)
    #zeitdifferenz = models.CharField(max_length=50)
    #bearbeitungszeit = models.CharField(max_length=50)
    #unterbrechungszeit = models.CharField(max_length=50)
    #zurückgelegte_strecke = models.CharField(max_length=50)
    #durchschnittliche_fahrgeschwindigkeit = models.CharField(max_length=50)
    #bearbeitungsbreite = models.CharField(max_length=50)
    #bearbeitetNutzfläche = models.CharField(max_length=50)
    #flächenleistung = models.CharField(max_length=50)

    def __str__(self):
        return self.massnahme
