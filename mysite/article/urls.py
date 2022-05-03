from django.urls import URLPattern, path
from . import views

app_name="article"

urlpatterns=[
    path('article-column/',views.article_column,name="article_column")
]