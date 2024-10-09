from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Modelo de autenticação customizado
class CustomUser(AbstractUser):
    access_level = models.IntegerField(default=1)

# Modelo para cadastro das propriedades
class EnvironmentalData(models.Model):   
    propriedade = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=200)
    content = models.TextField()
    required_access_level = models.IntegerField(default=1)

    def __str__(self):
        return self.title