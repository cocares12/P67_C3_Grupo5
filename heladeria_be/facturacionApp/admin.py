from django.contrib import admin
from .models.venta import Venta
from .models.usuario import Usuario
from .models.producto import Producto
from .models.proveedor import Proveedor
from .models.cliente import Cliente

admin.site.register(Venta)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Cliente)

# Register your models here.
