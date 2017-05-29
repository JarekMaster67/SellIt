from django.db import models

class Items(models.Model):
    login = models.CharField(max_length=250)
    tytul = models.CharField(max_length=250)
    kategoria = models.CharField(max_length=250)
    zdjecie = models.CharField(max_length=1000)
    lokalizacja = models.CharField(max_length=200)

    def __str__(self):
        return self.login + ' - ' + self.tytul

class Item(models.Model):
    Items = models.ForeignKey(Items,on_delete=models.CASCADE)
    opis = models.CharField(max_length=4000)

