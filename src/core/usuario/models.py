from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from .send_email import send
import uuid
from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    token = models.CharField(max_length=255, unique=True, default=None, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]

class Worker(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='worker', default=None)
    cod_worker = models.CharField(max_length=20)
    class PositionChoices(models.TextChoices):
        PROOFREADER = 'revisor', 'Revisor'
        EXPEDITION = 'expedição', 'Expedição'
    position = models.CharField(max_length=12, choices=PositionChoices.choices, default=PositionChoices.EXPEDITION)

    def __str__(self):
        return self.user.email
    
@receiver(post_save, sender=Worker)
def accept_worker(instance, sender, created, **kwargs):
    if created: 
        user = Usuario.objects.get(email=instance.user)
        try:
            token = str(uuid.uuid4())
            user.token = token
            user.save()
            send(instance, token)
        except Usuario.DoesNotExist as e:
            return Exception(f'error: {str(e)}')

    
