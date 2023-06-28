from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from tag.models import Tag


class User(AbstractUser):
    bio = models.TextField(_("bio"), max_length=500, blank=True)
    is_admin = models.BooleanField(_("admin"), default=False)
    avatar = models.ImageField("Аватар", upload_to="profile/avatars/", blank=True, null=True)
    background = models.ImageField("Бєкграунд", upload_to="profile/backgrounds/", blank=True, null=True)
    tag = models.ManyToManyField(Tag, related_name='users', blank=True)

class UserTag(models.Model):
    user = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, related_name='user_tags')
    tag = models.ForeignKey(Tag, verbose_name="Тег", on_delete=models.CASCADE, related_name='user_tags')
    count = models.PositiveIntegerField(default=0)

    def increment_count(self):
        self.count += 1
        self.save()

    def __str__(self):
        return f'{self.user.username} - {self.tag.text}'