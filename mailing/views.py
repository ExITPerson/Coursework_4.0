from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView

from mailing.forms import RecipientForm, MessageForm, MailingForm
from mailing.models import Recipient, Message, Mailing
from mailing.services import MailingServices


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


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/front_mailing/create_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/front_mailing/create_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing/front_mailing/delete_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailsView(DetailView):
    model = Mailing
    template_name = 'mailing/front_mailing/mailing_details.html'
    context_object_name = 'mailing'


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/front_mailing/mailing_list.html'
    context_object_name = 'mailings'


class MailingSendView(View):
    def get(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        return render(request, 'mailing/front_mailing/mailing_send.html', {'mailing': mailing})

    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        response = MailingServices.send_mailing(mailing)
        messages.success(request, response)
        return redirect(reverse('mailing:mailing_details', kwargs={'pk':pk}))