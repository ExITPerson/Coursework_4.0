from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from mailing.models import MailingAttempt


class MailingServices:

    @staticmethod
    def send_mailing(mailing):
        if mailing.status == 'running':
            return "Рассылка уже запущена"

        mailing.status = 'running'
        mailing.first_shipment = timezone.now()
        mailing.save()

        all_successfully = True

        for recipient in mailing.recipients.all():
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.letter,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[recipient.email]
                )

                status = 'successfully'
                response = 'Письмо отправлено'

            except Exception as e:
                status = 'not successfully'
                response = 'Письмо не отправлено'
                all_successfully = False


            MailingAttempt.objects.create(
                datetime=timezone.now(),
                status= 'successfully' if status else 'not successfully',
                response_mail_server = response,
                mailing=mailing
            )

        mailing.status = 'completed'
        mailing.last_shipment = timezone.now()
        mailing.save()

        if all_successfully:
            return 'Все письма отправлены'
        else:
            return 'Рассылка завершена с ошибкой, смотреть логи'
