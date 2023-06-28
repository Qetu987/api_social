from django.db import models
from user.models import User
from tag.models import Tag

# Create your models here.
class Photo(models.Model):
    title = models.CharField('Название', max_length=300)
    text = models.TextField('Текст фото', blank=True, null=True)
    poster = models.ImageField("Постер", upload_to="Photo/", blank=True, null=True)
    draft = models.BooleanField("Черновик", default=False)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, related_name='photo')
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания", blank=True)
    tag = models.ManyToManyField(Tag, verbose_name='теги', related_name='photo')
    
    def __str__(self):
        return f'{self.title}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos_likes')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)


class Reviews(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos_reviews')
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', related_name='parent_reviews', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True)
    tread = models.ForeignKey('self', related_name='tread_reviews', verbose_name='Тред', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ForeignKey(Photo, verbose_name="Фото", on_delete=models.CASCADE, related_name='Reviews')
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания", blank=True)

    def __str__(self):
        return f"{self.owner} - {self.photo} - {self.id}"
    

class Reviews_like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo_review_like')
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, related_name='review_likes')
    created = models.DateTimeField(auto_now_add=True)