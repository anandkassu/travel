from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Destination

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

def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})