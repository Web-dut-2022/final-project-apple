from django.urls import path,re_path
from . import views

app_name="article"

urlpatterns=[
    path('article-column/',views.article_column, name="article_column"),
    path('article-list/',views.article_list, name="article_list"),
    path('del-article/',views.del_article, name="del_article"),
    path('redit-article/<int:article_id>',views.redit_article, name="redit_article"),
]