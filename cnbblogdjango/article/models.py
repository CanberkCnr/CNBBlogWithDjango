from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
#ck editoru ekleme ksımımız.
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateField(auto_now_add = True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name = "Makaleye Fotoğraf Ekleyiniz" )
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
    #en son eklenen makale ilk gösterilmiş olur.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name= 'makale', related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=400,verbose_name = "Yorum")
    comment_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
    #en son eklenen makale ilk gösterilmiş olur.

