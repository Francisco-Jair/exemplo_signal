from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.usuario.username


def criar_profile(sender, instance, created, **kwargs):
    """
    sender -> Vai ser o modelo
    instace -> Objeto 
    created -> verdadeiro ou falso, vai ser vdd so quando o objeto vai ser criado
    **kwargs -> 
    """
    if created:
        Profile.objects.create(usuario=instance)


post_save.connect(criar_profile, sender=User)