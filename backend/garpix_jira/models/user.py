from django.db import models
from .server import Server


class User(models.Model):
    email = models.CharField(max_length=512, verbose_name='Почта')
    display_name = models.CharField(blank=True, default='', max_length=512, verbose_name='Отображаемое имя')
    user_key = models.CharField(max_length=50, verbose_name='Ключ пользователя')
    server = models.ForeignKey(Server, verbose_name='Сервер Jira', on_delete=models.CASCADE)
    user_tracks_time = models.BooleanField(default=True, verbose_name='Пользователь трекает время?')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if self.display_name != '':
            return self.display_name
        return self.email

    @staticmethod
    def sync(server: Server):
        jira = server.auth()
        users = jira.search_users('""', maxResults=300)
        for user in users:
            user_dict = {
                'display_name': user.displayName,
                'email': user.emailAddress,
                'user_key': user.key,
                'server': server,
            }
            obj, created = User.objects.update_or_create(
                user_key=user_dict['user_key'],
                defaults=user_dict,
            )
