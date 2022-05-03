from django import forms
from .models import ArticleColumn

class ArticleColumnForm(forms.ModelForm):
    class meta:
        model=ArticleColumn
        fields=("column",)