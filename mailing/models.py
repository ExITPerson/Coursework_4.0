from django.db import models

from config import settings


class Recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите электронную почту')
    full_name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipients',
        verbose_name='Автор',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'
        ordering = ['full_name',]
        permissions = [
            ('can_list_all_recipients_view', 'Can list all recipients view',),
        ]


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Тема письма', help_text='Тема письма')
    letter = models.TextField(verbose_name='Письмо')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Автор',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['subject',]


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана',),
        ('running', 'Запущена',),
        ('completed', 'Завершена',)
    ]
    name = models.CharField(max_length=150, verbose_name='Название')
    first_shipment = models.DateTimeField(null=True, blank=True, editable=False)
    last_shipment = models.DateTimeField(null=True, blank=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='mailings')
    recipients = models.ManyToManyField(Recipient)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mailings',
        verbose_name='Автор',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Mailing {self.id} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ('can_disabling_mailings', 'Disabling mailings',),
            ('can_mailing_static_view', 'Can mailing static view'),
            ('can_list_all_mailing_view', 'Can list all mailing view',),
        ]


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('successfully', 'Успешно',),
        ('not successfully', 'Не успешно',)
    ]

    datetime = models.DateTimeField(null=True, blank=True, editable=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='not successfully', verbose_name='Статус')
    response_mail_server = models.TextField()
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='mailing')

    def __str__(self):
        return f"Mailing {self.id} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
