from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView

from mailing.forms import RecipientForm, MessageForm
from mailing.models import Recipient, Message


class HomeTemplateView(TemplateView):
    template_name = 'mailing/home.html'


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing/recipient/create_recipient.html'
    success_url = reverse_lazy('mailing:recipient_details')


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing/recipient/create_recipient.html'
    success_url = reverse_lazy('mailing:recipient_details')


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'mailing/recipient/delete_recipient.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientDetailsView(DetailView):
    model = Recipient
    template_name = 'mailing/recipient/recipient_details.html'
    context_object_name = 'recipient'


class RecipientListView(ListView):
    model = Recipient
    template_name = 'mailing/recipient/recipients_list.html'
    context_object_name = 'recipients'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message/create_message.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message/create_message.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailing/message/delete_message.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailsView(DetailView):
    model = Message
    template_name = 'mailing/message/message_details.html'
    context_object_name = 'message'


class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message/message_list.html'
    context_object_name = 'messages'