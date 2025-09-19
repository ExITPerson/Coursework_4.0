from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms
from django.core.exceptions import ValidationError


User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                if not user.is_active:
                    raise ValidationError("Ваш аккаунт заблокирован. Вход невозможен.", code='inactive')
            except User.DoesNotExist:
                pass

        return super().clean()