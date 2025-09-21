from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms
from django.core.exceptions import ValidationError


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

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'full_name', 'phone_number', 'country',)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['avatar'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Загрузите аватар'
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите Ф.И.О.'
            }
        )

        self.fields['phone_number'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }
        )

        self.fields['country'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите страну'
            }
        )
