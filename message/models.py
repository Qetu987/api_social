from django.db import models
from user.models import User


class Group(models.Model):
    name = models.CharField('Название', max_length=300)
    desc = models.CharField('Описание', max_length=500, blank=True, null=True)
    users = models.ManyToManyField(User, verbose_name='Учасники чата', related_name='group')
    draft = models.BooleanField("Черновик", default=False)
    is_hide = models.BooleanField("Спрятан", default=False)
    is_private = models.BooleanField("Приватний", default=True)

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, related_name='message')
    text = models.CharField('Описание', max_length=500, blank=True, null=True)
    recipient = models.ForeignKey(Group, verbose_name="Чат", on_delete=models.CASCADE, related_name='message')
    draft = models.BooleanField("Черновик", default=False)
    is_read = models.BooleanField("Прочитан", default=False)
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания", blank=True)

    def __str__(self):
        return f'{self.text}'
