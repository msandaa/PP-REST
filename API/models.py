from django.db import models



class Produkte(models.Model):

    produkte = models.ManyToManyField('self',related_name='produkt', blank=True ,symmetrical=False)
    agrarprodukt = models.ForeignKey('Agrarprodukte',related_name='produkt',blank=True, null=True, on_delete=models.PROTECT)

    produktname = models.CharField(max_length=50)
    produktbeschreibung = models.TextField(max_length=300)

    def __str__(self):
         return self.produktname

class Produktmassnahmen(models.Model):

    produkt = models.ForeignKey('Produkte', related_name='produktmassnahmen', on_delete=models.PROTECT)

    massnahme = models.CharField(max_length=50)
    beschreibung = models.TextField(max_length=300)

    def __str__(self):
         return self.massnahme


class Agrarprodukte(models.Model):

   agrarprodukt = models.CharField(max_length=50)
   los_chargennummer = models.CharField(max_length=50)

   produktionsart = models.CharField(max_length=50)

   produzent_name = models.CharField(max_length=50)
   produzent_straße = models.CharField(max_length=50)
   produzent_ort = models.CharField(max_length=50)

   def __str__(self):
       return self.agrarprodukt

class Nutzflaechen(models.Model):

#Nutzflächen!!! Bei verantowrtlicher plural benutzen!! Dann benso in UsersSerializer ändern

    verantwortlicher = models.ForeignKey('auth.User', related_name='nutzflaeche', on_delete=models.PROTECT)
    agrarprodukt = models.OneToOneField(Agrarprodukte, related_name = 'nutzflaeche', on_delete=models.CASCADE)

    boxnummer = models.IntegerField()
    nutzflaechennummer = models.IntegerField()

    kreisnummer = models.IntegerField()
    kreis = models.CharField(max_length=50)
    bundeslandnummer = models.IntegerField()
    bundelsland = models.CharField(max_length=50)

    nutzflaeche = models.FloatField()

    def __str__(self):
        return str(self.nutzflaechennummer)

class Nutzflaechenmassnahmen(models.Model):

    verantwortlicher = models.ForeignKey('auth.User', related_name='nutzflaechenmassnahmen', on_delete=models.PROTECT)
    nutzflaeche = models.ForeignKey(Nutzflaechen, related_name='nutzflaechenmassnahmen',on_delete=models.CASCADE)

    massnahme = models.CharField(max_length=50)
    landwirtschftliches_nutzfahrzeug = models.CharField(max_length=50)

    datum = models.DateTimeField()

    startuhrzeit_der_bearbeitung = models.TimeField(auto_now=False, auto_now_add=False)
    enduhrzeit_der_bearbeitung = models.TimeField(auto_now=False, auto_now_add=False)
    zeitdifferenz = models.TimeField(auto_now=False, auto_now_add=False)
    bearbeitungszeit = models.TimeField(auto_now=False, auto_now_add=False)
    unterbrechungszeit = models.TimeField(auto_now=False, auto_now_add=False)

    zurückgelegte_strecke = models.FloatField()
    durchschnittliche_fahrgeschwindigkeit = models.FloatField()
    bearbeitungsbreite = models.FloatField()
    bearbeitet_nutzfläche = models.FloatField()
    flächenleistung = models.FloatField()

    def __str__(self):
        return self.massnahme
