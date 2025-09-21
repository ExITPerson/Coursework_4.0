from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from django.apps import apps

User = apps.get_model(settings.AUTH_USER_MODEL)

class Command(BaseCommand):
    def handle(self, *args, **options):
        group_name = 'Managers'
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            permissions = Permission.objects.filter(codename__in=[
                'add_mailing', 'add_recipient', 'add_message',
                'delete_mailing', 'delete_recipient', 'delete_message',
                'view_mailing', 'view_recipient', 'view_message',
                'change_mailing', 'change_recipient', 'change_message',
                'view_user', 'can_blocking_user', 'can_list_user_view', 'can_list_all_recipients_view',
                'can_list_all_mailing_view', 'can_disabling_mailings'

            ])
            group.permissions.set(permissions)
            self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" создана'))
        else:
            self.stdout.write(f'Группа "{group_name}" уже существует')



        user_name = 'BAD'
        user, created_user = User.objects.get_or_create(email='manager@example.com', full_name=user_name)
        if created_user:
            user.set_password('1234')
            user.is_active = True
            user.is_staff = True
            user.groups.add(group)
            self.stdout.write(f'Пользователь "{user_name}" добавлен в группу "{group_name}"')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Пользователь "{user_name}" создан'))
        else:
            self.stdout.write(f'Пользователь "{user_name}" уже существует')

