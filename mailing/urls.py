from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import HomeTemplateView, RecipientListView, RecipientDetailsView, RecipientDeleteView, \
    RecipientCreateView, RecipientUpdateView, MessageListView, MessageDetailsView, MessageDeleteView, MessageCreateView, \
    MessageUpdateView, MailingListView, MailingDetailsView, MailingDeleteView, MailingCreateView, MailingUpdateView, \
    MailingSendView, BaseUserView, MailingDisableView

app_name = MailingConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),

    path('recipients_list/', RecipientListView.as_view(), name='recipients_list'),
    path('recipient_details/<int:pk>/', RecipientDetailsView.as_view(), name='recipient_details'),
    path('<int:pk>/recipient_delete/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('create_recipient/', RecipientCreateView.as_view(), name='create_recipient'),
    path('<int:pk>/update_recipient/', RecipientUpdateView.as_view(), name='update_recipient'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_details/<int:pk>/', MessageDetailsView.as_view(), name='message_details'),
    path('<int:pk>/delete_message/', MessageDeleteView.as_view(), name='delete_message'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('<int:pk>/update_message/', MessageUpdateView.as_view(), name='update_message'),

    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_details/<int:pk>', MailingDetailsView.as_view(), name='mailing_details'),
    path('<int:pk>/delete_mailing/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('<int:pk>/update_mailing/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing_details/<int:pk>/send/', MailingSendView.as_view(), name='mailing_send'),
    path('mailing/<int:pk>/disable/', MailingDisableView.as_view(), name='mailing_disable'),

    path('users/', BaseUserView.as_view(), name='user_list'),
]