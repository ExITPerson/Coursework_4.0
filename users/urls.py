from django.contrib.auth import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
from django.views.decorators.cache import cache_page

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserLoginView, UserListView, UserDetailView, \
    BlockingUserView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', cache_page(60*15)(UserLoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', cache_page(60*15)(UserCreateView.as_view()), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('user_list/', cache_page(60*15)(UserListView.as_view()), name='user_list'),
    path('user_details/<int:pk>/', cache_page(60)(UserDetailView.as_view()), name='user_details'),
    path('users/<int:user_id>/block/', BlockingUserView.as_view(), name='block_user'),

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