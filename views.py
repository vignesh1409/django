from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth


# Create your views here.

def login(request):
     if request.method=='POST':
          username=request.POST["username"]
          password=request.POST['password']

          user=auth.authenticate(username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect('/travello')
          else:
               messages.info(request,'INVALID CREDENTIALS')
               return redirect('register')

     else:
          return render(request,'login.html')

def register(request):

    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['mailid']
        if password1!=password2:
             messages.error(request,'PASSWORD NOT MATCHING')
             return redirect('register')
        if User.objects.filter(username=username).exists():
             messages.info(request,'USERNAME ALREADY TAKEN')
             return redirect('register')
        if User.objects.filter(email=email).exists():
             messages.info(request,'EMAIL ID ALREADY EXSITS')
             return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
            user.save();
            return redirect('login')



    else:    
        return render(request,'register.html')


def logout(request):
     auth.logout(request)
     return redirect('/travello')