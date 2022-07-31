from django import forms
from django.forms import ModelForm
from .models import Article
#Daha önceden oluşturduğumuz article class'ımızı kullanabilmek için

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image",]
        
