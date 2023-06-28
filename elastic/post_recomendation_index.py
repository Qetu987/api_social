# from elasticsearch import Elasticsearch
# from django.conf import settings


# def index_posts():
#     es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])  # Укажите соответствующий хост и порт Elasticsearch
#     es.indices.create(index=settings.ELASTICSEARCH_INDEX, ignore=400)

#     # Получите все посты, которые вы хотите проиндексировать
#     posts = Post.objects.all()

#     for post in posts:
#         # Создайте документ для индексации в Elasticsearch
#         doc = {
#             'title': post.title,
#             'text': post.text,
#             # Добавьте другие необходимые поля из модели Post
#             'tag': [tag.text for tag in post.tag.all()]
#         }

#         # Выполните индексацию документа в Elasticsearch
#         es.index(index=settings.ELASTICSEARCH_INDEX, body=doc)

# # Вызовите функцию index_posts() для индексации постов
# index_posts()