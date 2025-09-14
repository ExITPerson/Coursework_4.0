from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView

from mailing.forms import RecipientForm
from mailing.models import Recipient


class HomeTemplateView(TemplateView):
    template_name = 'mailing/home.html'


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing/create_recipient.html'
    success_url = reverse_lazy('mailing:recipient_details')


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing/create_recipient.html'
    success_url = reverse_lazy('mailing:recipient_details')


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'mailing/delete_recipient.html'
    success_url = reverse_lazy('mailing:recipient_list')

class RecipientDetailsView(DetailView):
    model = Recipient
    template_name = 'mailing/recipient_details.html'
    context_object_name = 'recipient'

class RecipientListView(ListView):
    model = Recipient
    template_name = 'mailing/recipients_list.html'
    context_object_name = 'recipients'