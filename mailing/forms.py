from django import forms

from mailing.models import Recipient, Message, Mailing


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['email', 'full_name', 'comment']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'letter']


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['name', 'message', 'recipients']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['recipients'].queryset = Recipient.objects.filter(author=user)
