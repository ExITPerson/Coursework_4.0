from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import HomeTemplateView, RecipientListView, RecipientDetailsView, RecipientDeleteView, \
    RecipientCreateView, RecipientUpdateView

app_name = MailingConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('recipients_list/', RecipientListView.as_view(), name='recipients_list'),
    path('recipient_details/<int:pk>/', RecipientDetailsView.as_view(), name='recipient_details'),
    path('<int:pk>/recipient_delete/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('create_recipient/', RecipientCreateView.as_view(), name='create_recipient'),
    path('<int:pk>/update_recipient/', RecipientUpdateView.as_view(), name='update_recipient'),
]