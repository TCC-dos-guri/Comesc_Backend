from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )

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