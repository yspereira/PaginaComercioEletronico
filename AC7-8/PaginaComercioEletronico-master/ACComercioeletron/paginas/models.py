from django.db import models

# Create your models here.
 
class Usuario(models.Model):
    email = models.EmailField("email", max_length=50)
    senha = models.CharField("senha", max_length=14)
    nome = models.CharField("nome", max_length=40)
    dataNascimento = models.CharField("dataNascimento", max_length=10)

    def __str__(self):
        return self.email

class ListaPresenca(models.Model):
    nome = models.CharField("nome", max_length=40)
    email = models.EmailField("email", max_length=40)
    nascimento = models.CharField("dataNascimento", max_length=10)

    def __str__(self):
        return self.nome
