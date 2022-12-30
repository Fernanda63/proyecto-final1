from django.db import models

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.direccion}, {self.id}"


from django.db import models

class Amigo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
      return f"{self.nombre}, {self.id}"



     