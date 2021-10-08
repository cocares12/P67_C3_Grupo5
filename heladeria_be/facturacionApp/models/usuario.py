from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Crea y guarda un usuario con el usuario y conraseña dados.
        """
        if not username:
            raise ValueError('Los usuarios deben tener un nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Crea y guarda un supersuario con el usuario y conraseña dados.
        """
        user = self.create_user(
            username=username,
            password=password,
        )       
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    idUsuario = models.BigIntegerField('Identificación',primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)

    TIPO_DE_USUARIO=[
        ('VN','Vendedor'),
        ('AD', 'Administrador'),
    ]
    tipoUsuario=models.CharField(
        max_length = 2,
        choices = TIPO_DE_USUARIO,
        default = 'VN',
    )

    nombreUsuario = models.CharField('Nombre del usuario', max_length = 50)
    apellidoUsuario = models.CharField('Apellido del usuario', max_length = 50)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'
