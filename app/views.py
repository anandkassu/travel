from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Destination
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import ExpenseItem, Message
from .form import ContactForm

@csrf_exempt
# def home(request):
#     return render(request, 'home(1).html',{'sum':'addition of two number'})

# def add(request):
#     var1=int(request.POST["num1"])
#     var2=int(request.POST["num2"])
#     res=var1+var2
#     return render(request, 'result.html',{'result':res})


    
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

#budgets
@login_required
def home(request):
    return render(request, 'home.html')


class AddItemView(CreateView):
    queryset = ExpenseItem.objects.all()
    template_name = 'add_new.html'
    fields = ['title', 'date', 'amount', 'description', 'account', 'category']
    success_url = '/budget'





class ListItemView(ListView):
    queryset = ExpenseItem.objects.all()
    template_name = 'view_expense.html'


class DetailItemView(DetailView):
    queryset = ExpenseItem.objects.all()
    template_name = 'expenseitem_detail.html'



class UpdateItemView(UpdateView):
    queryset = ExpenseItem.objects.all()
    fields = ['title', 'date', 'amount', 'description', 'account', 'category']
    template_name = 'budgets/expenseitem_form.html'

    def get_success_url(self):
        return '/view/' + str(self.object.id)


class DeleteItemView(DeleteView):
    queryset = ExpenseItem.objects.all()
    fields = ['title', 'date', 'amount', 'description', 'account', 'category']
    template_name = 'budgets/expenseitem_confirm_delete.html'

    def get_success_url(self):
        return '/budget'


@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('validated')
            Message.objects.create(title=request.POST.get('title'), email=request.POST.get('email'),
                                   message=request.POST.get('message'))
            return HttpResponseRedirect('/')

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact_form.html', context)