from django.db import models

class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):  # def __str__ permet d'afficher le nom dans le pannel admin à la place de pizza Object
        return self.nom 