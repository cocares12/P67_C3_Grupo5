from django.db import models

class Proveedor(models.Model):
    idProveedor = models.BigAutoField(primary_key = True)
    nombreProveedor = models.CharField('Nombre del proveedor', max_length = 50)
    direccionProveedor = models.CharField('Dirección', max_length = 50)
    numeroTelefonicoProveedor = models.CharField('Numero telefónico', max_length = 20)