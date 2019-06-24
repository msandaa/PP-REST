from django.db import models

class Produkte(models.Model):

    besteht_aus_produkte = models.ManyToManyField('self',related_name='produkt', blank=True ,symmetrical=False)
    hergestellt_aus_agrarprodukt = models.ForeignKey('Agrarprodukte',related_name='wird_verwendet_in_produkte',blank=True, null=True, on_delete=models.SET_NULL)
    # SET_NULL - Pordukt soll nicht gelöscht werden, wenn Agrarproduk gelöscht wird

    produktname = models.CharField(max_length=50)
    produktbeschreibung = models.TextField(max_length=300)

    def __str__(self):
         return self.produktname

class Produktmassnahmen(models.Model):

    produkt = models.ForeignKey('Produkte', related_name='produktmassnahmen', on_delete=models.CASCADE)
    # CASCADE - Produktmassnahmen werden gelöscht wenn dazugehöriges Produkt gelöscht wird

    massnahme = models.CharField(max_length=50)
    beschreibung = models.TextField(max_length=300)

    def __str__(self):
         return self.massnahme


class Agrarprodukte(models.Model):

    angebaut_auf_nutzflaeche = models.OneToOneField('Nutzflaechen', related_name = 'agrarprodukt', on_delete=models.PROTECT)

    agrarprodukt = models.CharField(max_length=50)
    los_chargennummer = models.CharField(max_length=50)

    produktionsart = models.CharField(max_length=50)

    produzent_name = models.CharField(max_length=50)
    produzent_straße = models.CharField(max_length=50)
    produzent_ort = models.CharField(max_length=50)

    def __str__(self):
        return self.agrarprodukt

class Nutzflaechen(models.Model):

    verantwortlicher = models.ForeignKey('auth.User', related_name='nutzflaeche',blank=True, null=True, on_delete=models.SET_NULL)
    # SET_NULL - Nutzflaeche soll nicht gelöscht werden, wenn verantwortlicher gelöscht wird

    boxnummer = models.IntegerField()
    nutzflaechennummer = models.IntegerField()

    kreisnummer = models.IntegerField()
    kreis = models.CharField(max_length=50)
    bundeslandnummer = models.IntegerField()
    bundesland = models.CharField(max_length=50)

    nutzflaeche_in_ha = models.FloatField()

    def __str__(self):
        return str(self.nutzflaechennummer)

class Nutzflaechenmassnahmen(models.Model):

    verantwortlicher = models.ForeignKey('auth.User', related_name='nutzflaechenmassnahmen', blank=True, null=True, on_delete=models.SET_NULL)
    # SET_NULL - Nutzflaechenmassnahme soll nicht gelöscht werden, wenn verantwortlicher gelöscht wird
    ausgeführt_auf_nutzflaeche = models.ForeignKey(Nutzflaechen, related_name='nutzflaechenmassnahmen',on_delete=models.CASCADE) #wie erricht man, das der Frmeschlüssel nichtmehr geänder werden kann ?
    # CASCADE - Nutzflaechenmassnahmen werden gelöscht wenn dazugehöriges Nutzflaeche gelöscht wird

    massnahme = models.CharField(max_length=50)
    landwirtschftliches_nutzfahrzeug = models.CharField(max_length=50)

    datum = models.DateTimeField()

    startuhrzeit_der_bearbeitung = models.TimeField(auto_now=False, auto_now_add=False)
    enduhrzeit_der_bearbeitung = models.TimeField(auto_now=False, auto_now_add=False)
    zeitdifferenz = models.TimeField(auto_now=False, auto_now_add=False)
    bearbeitungszeit = models.TimeField(auto_now=False, auto_now_add=False)
    unterbrechungszeit = models.TimeField(auto_now=False, auto_now_add=False)

    zurückgelegte_strecke_in_km = models.FloatField()
    durchschnittliche_fahrgeschwindigkeit_in_kmh = models.FloatField()
    bearbeitungsbreite_in_m = models.FloatField()
    bearbeitet_nutzfläche_in_ha = models.FloatField()
    flächenleistung_in_hah = models.FloatField()

    def __str__(self):
        return self.massnahme
