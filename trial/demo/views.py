from django.shortcuts import render,HttpResponse
from .models import Users

# Create your views here.

def home(request):
    return render(request,"home.html")


def users(request):
    items = Users.objects.all()
    return render (request,"users.html",{"users":items})

def adduser(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        no = request.POST['no']

        newUser = Users(username =username  ,  password =password , no =no)
        newUser.save()
    
    return render(request,"adduser.html")
