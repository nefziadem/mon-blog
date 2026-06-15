from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
    
class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.date_envoi.strftime('%d/%m/%Y')}"