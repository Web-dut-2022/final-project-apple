from django import forms
from .models import ArticleColumn, ArticlePost

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model=ArticleColumn
        fields=("column",)

class AritclePostForm(forms.ModelForm):
    class Meta:
        model=ArticlePost
        fields=("title","body")