from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    slug = models.SlugField('Slug', unique=True)
    text = models.CharField('Text', max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)  # Генерируем слаг на основе заголовка
        super(Tag, self).save(*args, **kwargs)