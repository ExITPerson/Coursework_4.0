from django.contrib import admin
from .models import Recipient, Message, Mailing, MailingAttempt


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name',)
    search_fields = ('email', 'full_name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject',)
    search_fields = ('subject',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('message', 'status',)
    search_fields = ('message', 'status',)


@admin.register(MailingAttempt)
class MailingAttempt(admin.ModelAdmin):
    list_display = ('datetime', 'status', 'mailing',)
    search_fields = ('status',)