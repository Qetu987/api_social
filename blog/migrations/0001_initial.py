# Generated by Django 4.2.2 on 2023-06-16 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст поста')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Постер')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('tag', models.ManyToManyField(related_name='Post', to='tag.tag', verbose_name='теги')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_reviews', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_reviews', to='blog.reviews', verbose_name='Родитель')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reviews', to='blog.post', verbose_name='Пост')),
                ('tread', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tread_reviews', to='blog.reviews', verbose_name='Тред')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_likes', to='blog.reviews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_review_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
