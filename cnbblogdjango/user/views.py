from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
#Login fonksiyonumuzu kullanmak istediğimizi söylüyoruz.


# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    #Get request olsa bile None döneceği için Form yine oluşur.
    if request.method == "POST":
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            newUser.is_active = True
            newUser.save()

            login(request,newUser)
            messages.success(request,"Başarıyla Kayıt Oldunuz")
            
            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"templates/register.html",context)
    context = {
            "form" : form
    }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    
    context = {
        "form" : form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        #Authenticate method'u giderek database'e bakar ve kontrol eder, eğer varsa döner.

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request, "login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        #Login işlemi için kullanılır.
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yaptınız")
    return redirect("index")