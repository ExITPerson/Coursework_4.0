from django.core.management.base import BaseCommand, CommandError
from mailing.models import Mailing
from mailing.services import MailingServices
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int, help='ID рассылки для отправки')
        parser.add_argument(
            '--author_id',
            type=int,
            help='ID пользователя-автора (необязательно)',
            default=None
        )

    def handle(self, *args, **options):
        mailing_id = options['mailing_id']
        author_id = options['author_id']

        try:
            mailing = Mailing.objects.get(id=mailing_id)
        except Mailing.DoesNotExist:
            raise CommandError(f'Рассылка с ID {mailing_id} не найдена.')

        author = None
        if author_id:
            try:
                author = User.objects.get(id=author_id)
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Пользователь с ID {author_id} не найден. Используется author=None'))

        self.stdout.write(f'Запуск рассылки ID {mailing_id}...')

        result = MailingServices.send_mailing(mailing, author=author)

        self.stdout.write(self.style.SUCCESS(f'Результат: {result}'))