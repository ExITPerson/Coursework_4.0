from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView

from mailing.forms import RecipientForm, MessageForm, MailingForm
from mailing.models import Recipient, Message, Mailing


class HomeTemplateView(TemplateView):
    template_name = 'front_mailing/home.html'


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'front_mailing/recipient/create_recipient.html'
    success_url = reverse_lazy('front_mailing:recipient_details')


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'front_mailing/recipient/create_recipient.html'
    success_url = reverse_lazy('front_mailing:recipient_details')


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'front_mailing/recipient/delete_recipient.html'
    success_url = reverse_lazy('front_mailing:recipient_list')


class RecipientDetailsView(DetailView):
    model = Recipient
    template_name = 'front_mailing/recipient/recipient_details.html'
    context_object_name = 'recipient'


class RecipientListView(ListView):
    model = Recipient
    template_name = 'front_mailing/recipient/recipients_list.html'
    context_object_name = 'recipients'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'front_mailing/message/create_message.html'
    success_url = reverse_lazy('front_mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'front_mailing/message/create_message.html'
    success_url = reverse_lazy('front_mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'front_mailing/message/delete_message.html'
    success_url = reverse_lazy('front_mailing:message_list')


class MessageDetailsView(DetailView):
    model = Message
    template_name = 'front_mailing/message/message_details.html'
    context_object_name = 'message'


class MessageListView(ListView):
    model = Message
    template_name = 'front_mailing/message/message_list.html'
    context_object_name = 'messages'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'front_mailing/front_mailing/create_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'front_mailing/front_mailing/create_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'front_mailing/front_mailing/delete_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailsView(DetailView):
    model = Mailing
    template_name = 'front_mailing/front_mailing/mailing_details.html'
    context_object_name = 'mailing'


class MailingListView(ListView):
    model = Mailing
    template_name = 'front_mailing/front_mailing/mailing_list.html'
    context_object_name = 'mailings'
