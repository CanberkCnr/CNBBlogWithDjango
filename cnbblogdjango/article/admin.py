from django.contrib import admin
from .models import Article,Comment

# Register your models here.
#admin.site.register(Article)
#Bu fonksiyon ,import işleminden sonra admin panelinde kaydetmemiz için kullanılır.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","author"]

    search_fields = ["title"]

    list_filter =  ["created_date"]

    class Meta:
        model = Article
        #Meta class'ı özel bir classtır ve Adı Meta olmalıdır. Modelimizi Article'a bağlarız.
    