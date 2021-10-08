from django.db import models

class Cliente(models.Model):
    idCliente = models.BigIntegerField('Identificacion', primary_key = True)
    nombreCliente = models.CharField('Nombre del cliente', max_length = 50)
    apellidoCliente = models.CharField('Apellido del cliente', max_length = 50)
    correoCliente = models.EmailField('Correo electronico', max_length = 100)