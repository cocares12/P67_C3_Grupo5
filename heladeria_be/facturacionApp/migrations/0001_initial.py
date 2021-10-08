# Generated by Django 3.2.7 on 2021-10-07 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('idUsuario', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Identificación')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('tipoUsuario', models.CharField(choices=[('VN', 'Vendedor'), ('AD', 'Administrador')], default='VN', max_length=2)),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='Nombre del usuario')),
                ('apellidoUsuario', models.CharField(max_length=50, verbose_name='Apellido del usuario')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Identificacion')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('apellidoCliente', models.CharField(max_length=50, verbose_name='Apellido del cliente')),
                ('correoCliente', models.EmailField(max_length=100, verbose_name='Correo electronico')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=300)),
                ('valorUnitario', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor unitario')),
                ('unidad', models.CharField(max_length=20, verbose_name='Unidad del producto')),
                ('cantidadExistencia', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Existencia')),
                ('composicion', models.CharField(max_length=50, verbose_name='Composición')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreProveedor', models.CharField(max_length=50, verbose_name='Nombre del proveedor')),
                ('direccionProveedor', models.CharField(max_length=50, verbose_name='Dirección')),
                ('numeroTelefonicoProveedor', models.CharField(max_length=20, verbose_name='Numero telefónico')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.BigAutoField(primary_key=True, serialize=False)),
                ('fechaVenta', models.DateTimeField(verbose_name='Fecha de venta')),
                ('cantidadProducto', models.BigIntegerField(verbose_name='Cantidad del producto')),
                ('impuesto', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='IVA')),
                ('subtotal', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Subtotal')),
                ('totalVenta', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='Total')),
                ('descuento', models.CharField(choices=[('SI', 'Aplica'), ('NO', 'No aplica')], default='NO', max_length=2)),
                ('formaPago', models.CharField(choices=[('EF', 'Efectivo'), ('TD', 'Tarjeta débito'), ('TC', 'Tarjeta de crédito')], default='EF', max_length=2)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='facturacionApp.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='facturacionApp.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='Proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Proveedor', to='facturacionApp.proveedor'),
        ),
    ]
