from django.contrib.auth import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserLoginView, UserListView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user_details/<int:pk>/', UserDetailView.as_view(), name='user_details'),

    path('reset_password/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        email_template_name="users/password_reset_email.html",
        success_url=reverse_lazy("users:password_reset_done"),
        subject_template_name='users/password_reset_subject.txt'
    ), name='reset_password'),
    path('reset_password/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url=reverse_lazy("users:password_reset_complete")
    ), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),
]