from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from users.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
