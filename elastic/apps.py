# elasticsearch/apps.py
from django.apps import AppConfig

class ElasticsearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elasticsearch'

    # def ready(self):
    #     from .post_recomendation_index import index_posts
    #     index_posts()