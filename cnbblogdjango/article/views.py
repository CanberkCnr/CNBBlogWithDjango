from cmath import log
from multiprocessing import context
from turtle import title
from webbrowser import get
from django.shortcuts import redirect,render,HttpResponse,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request, "about.html")

def articles(request):
    keyword = request.GET.get("keyword")
    
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles" : articles})

    articles = Article.objects.all()
    #Tüm articleları alarak bir listeye atar.
    return render(request,"articles.html",{"articles" : articles})

@login_required(login_url = 'user:login')
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html",context)

@login_required(login_url = 'user:login')
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("article:dashboard")
    form = {
        "form" : form
    }
    return render(request, "addarticle.html",form)

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article" : article,"comments" : comments})

@login_required(login_url = 'user:login')
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    #Article üzerinden objemizi alır ve yoksa 404 gönderir.
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
 
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("article:dashboard")
    
    return render(request,"update.html",{"form": form})

@login_required(login_url = 'user:login')
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        
        newComment.article = article

        newComment.save()
        
    return redirect(reverse("article:detail",kwargs = {"id":id}))