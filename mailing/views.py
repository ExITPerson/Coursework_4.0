from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView

from mailing.forms import RecipientForm, MessageForm, MailingForm
from mailing.models import Recipient, Message, Mailing, MailingAttempt
from mailing.services import MailingServices
from users.models import User


class HomeTemplateView(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mailings_count = Mailing.objects.all().count()
        mailings_running_count = Mailing.objects.filter(status='running').count()
        recipients_count = Recipient.objects.all().count()

        context['mailings_count'] = mailings_count
        context['mailings_running_count'] = mailings_running_count
        context['recipients_count'] = recipients_count

        return context

class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing/recipient/create_recipient.html'
    success_url = reverse_lazy('mailing:recipients_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing/recipient/create_recipient.html'
    success_url = reverse_lazy('mailing:recipient_details')


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    template_name = 'mailing/recipient/delete_recipient.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientDetailsView(LoginRequiredMixin, DetailView):
    model = Recipient
    template_name = 'mailing/recipient/recipient_details.html'
    context_object_name = 'recipient'


class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = 'mailing/recipient/recipients_list.html'
    context_object_name = 'recipients'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message/create_message.html'
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message/create_message.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mailing/message/delete_message.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailsView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'mailing/message/message_details.html'
    context_object_name = 'message'


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailing/message/message_list.html'
    context_object_name = 'messages'


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/front_mailing/create_mailing.html'
    login_url = 'users:login'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/front_mailing/create_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailing/front_mailing/delete_mailing.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailsView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailing/front_mailing/mailing_details.html'
    context_object_name = 'mailing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing = self.object

        messages_sent_successfully = MailingAttempt.objects.filter(mailing=mailing, status='successfully').count()
        messages_sent_not_successfully = MailingAttempt.objects.filter(mailing=mailing, status='not successfully').count()
        message_count = MailingAttempt.objects.filter(mailing=mailing).count()

        context['messages_sent_successfully'] = messages_sent_successfully
        context['messages_sent_not_successfully'] = messages_sent_not_successfully
        context['messages_sent_count'] = message_count

        return context


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailing/front_mailing/mailing_list.html'
    context_object_name = 'mailings'


class MailingSendView(LoginRequiredMixin, View):
    def get(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        return render(request, 'mailing/front_mailing/mailing_send.html', {'mailing': mailing})

    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        response = MailingServices.send_mailing(mailing, author=request.user)
        messages.success(request, response)
        return redirect(reverse('mailing:mailing_details', kwargs={'pk':pk}))


class BaseUserView(View):
    def get(self, request):
        users = User.objects.all()
        context = {
            'users': users,
            'current_user': request.user,
        }
        return render(request, 'mailing/base.html', context)


class MailingDisableView(LoginRequiredMixin, View):

    @method_decorator(permission_required('user.can_disabling_mailings', raise_exception=True))
    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)

        if mailing.status != 'running':
            messages.warning(request, 'Рассылка не запущена или уже завершена.')
            return redirect('mailing:mailing_details', pk=pk)

        mailing.status = 'disabled'
        mailing.save()

        messages.success(request, "Рассылка была принудительно остановлена.")
        return redirect('mailing:mailing_details', pk=pk)
