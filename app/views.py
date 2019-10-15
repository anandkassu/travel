from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Destination
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@csrf_exempt
def home(request):
    return render(request, 'home.html',{'sum':'addition of two number'})

def add(request):
    var1=int(request.POST["num1"])
    var2=int(request.POST["num2"])
    res=var1+var2
    return render(request, 'result.html',{'result':res})


# to pass data from here into html file


# def index(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.des = 'The City That Never Sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.des = 'First Biryani, Then Sherwani'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = 'Bengaluru'
    # dest3.des = 'Beautiful City'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 750
    # dest3.offer = True

    # destination = [dest1, dest2, dest3]

    # return render(request, "index.html", {'dests': destination})
    
# to pass data from database
def travel(request):
    return render(request, 'travel.html')

@login_required
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

def register(request):
    if request.method=='POST':
        # first_name=request.POST['first_name']
        # last_name=request.POST['last_name']    
        username=request.POST['username']
        email=request.POST['email'] 
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save();
                print('user created')
            
        else:
            messages.info(request,"password is not matching")
            return redirect('register')
        return redirect('login')

    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')