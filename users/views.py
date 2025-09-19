import secrets

from IPython.core.release import author
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from config.settings import EMAIL_HOST_USER
from mailing.models import MailingAttempt
from users.models import User
from users.forms import UserRegisterForm, UserAuthenticationForm
from django.contrib.auth.models import Group


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = secrets.token_hex(24)
        user.token = token
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message='Привет.\n'
                    'Перейди по ссылке ниже для завершения регистрации\n'
                    f'{url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    group = Group.objects.get(name='Users')
    user.groups.add(group)
    user.save()
    return redirect('users:login')


class UserLoginView(LoginView):
    authentication_form = UserAuthenticationForm
    template_name = 'users/login.html'


class BlockingUserView(LoginRequiredMixin, View):

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        if not request.user.has_perm('managers.can_blocking_user'):
            return HttpResponseForbidden

        user.is_active = not user.is_active
        user.save()

        return redirect('users:user_list')


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object

        success_count = MailingAttempt.objects.filter(status='successfully', author=user).count()
        failure_count = MailingAttempt.objects.filter(status='not successfully', author=user).count()
        messages_sent_count = MailingAttempt.objects.filter(author=user).count()

        context['success_count'] = success_count
        context['failure_count'] = failure_count
        context['messages_sent_count'] = messages_sent_count

        return context