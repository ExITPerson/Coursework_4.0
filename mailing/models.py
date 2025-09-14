from django.db import models


class Recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите электронную почту')
    full_name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.full_name


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Тема письма', help_text='Тема письма')
    letter = models.TextField(verbose_name='Письмо')

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана',),
        ('running', 'Запущена',),
        ('completed', 'Завершена',)
    ]

    first_shipment = models.DateTimeField()
    last_shipment = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='mailings')
    recipients = models.ManyToManyField(Recipient)

    def __str__(self):
        return f"Mailing {self.id} - {self.get_status_display()}"