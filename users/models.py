from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите электронную почту')
    full_name = models.CharField(max_length=150, verbose_name='Ф.И.О.')

    token = models.CharField(max_length=100, verbose_name='Token', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_blocking_user', 'Can blocking user',),
            ('can_list_user_view', 'Can list user view'),
        ]

    def __str__(self):
        return self.email
