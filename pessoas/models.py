from django.db import models
from django.db.models.fields import CharField, EmailField

class Pessoa(models.Model):
    nome = CharField(max_length=200)
    email = CharField(max_length=200)

    def __str__(self):
        return self.nome 