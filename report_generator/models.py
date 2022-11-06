from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES = (
	("1", "IN"),
	("2", "OUT")
)

class addReport(models.Model):
    heure = models.TimeField(auto_now_add=True)
    mouve = models.CharField(max_length=12, choices = CHOICES)
    nom_Visiteur = models.CharField(max_length=26)
    fonction = models.CharField(max_length=26)
    service = models.CharField(max_length=26)
    motif = models.CharField(max_length=26)
    phoneNumber = models.CharField(max_length=12, unique= True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
