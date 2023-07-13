from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import STATIC_URL

class User(AbstractUser):
    #agrego/modifico este atributo
    email = models.EmailField(max_length=200,unique=True,null=False,blank=False)
    #agrego una imagen de perfil
    image=models.ImageField(upload_to='user_images/%Y/%m/%d/')
    #le digo que atributo se utilizara para la autenticacion
    USERNAME_FIELD='email'
    #los campos requeridos para  un registro y no debe tener el USERNAME_FIELD (el email)
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def get_image(self):
        if self.image:
            return self.image.url
        return f'{STATIC_URL}media/img/empty_user.png'