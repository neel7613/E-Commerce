from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404, JsonResponse
from django.shortcuts import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *
from .models import Category,Device,Cart,Heavy_machine
from django.core.mail import send_mail,EmailMessage
from django.db.models import  Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        categories =  list(Category.objects.all().values_list('device_category',flat=True))
        
        if form.is_valid():
            user = form.save()
            
            login(request,user)
            
            user_id = user.id
            username = request.user.email
            
            context = {
                "categories" : categories,
                "usesrname"  : username
            }
            return HttpResponseRedirect(reverse('homepage'))
        
        else :
            context = {
                    "form" : form
            }
            return render(request,"register.html",context)
    
    form = NewUserForm()
    context = {
            "form" : form
    }
    return render(request,"register.html",context)



def single_slug(request,single_slug):

    cat = Category.objects.get(category_slug = single_slug)
    device = cat.device_set.all()
    
    context = {
        "devices" : device
    }

    return render(request,"devices.html",context)

        # if single_slug in categories:
        #
        #     matched_device = Device.objects.filter(device_category__device_category=single_slug)
        #
        #     return HttpResponse(f"{matched_device} is available")
        # else:
        #      return(HttpResponse(f"the device is not available"))
'''def logged_in(request,user_id):

    devices = Device.objects.all()
    categories = Category.objects.all()    
    
    if request.user.is_authenticated:
        #devices = Device.objects.all()
        username = request.user.email
        if 'search' in request.GET:
            devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
        
    context = {
        "devices" : devices,
        "username" : username,
        "categories" : categories
    }
    return render(request,"homepage.html",context)
    
    return render(request, 'homepage.html')'''

def homepage(request):
    
    user = False
    devices = Device.objects.all()
    categories = Category.objects.all()
    
    if request.user.is_authenticated:
        user = request.user
    
    if 'search' in request.GET:
        devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
    
    context = {
        "categories" : categories,
        "devices" : devices,
        "user" : user
    }
    return render(request,"homepage.html",context)


def log_in(request):

    devices = Device.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        
        if form.is_valid():
                                                                                            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username = username , password = password)
            
            if user is not None :
                login(request, user)
                
                if 'search' in request.GET:
                    devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
                
                context = {
                    "user": request.user,
                    "devices": devices,
                    "categories": categories
                }

                return HttpResponseRedirect(reverse('homepage'))

            else:
                messages.error(request,'username or password not correct')
                return redirect('log_in')

        else:
            messages.error(request,'username or password not correct')
            return redirect('log_in')
    
    form = AuthenticationForm()
    
    context = {
            "form" : form
    }
    return render(request,"login_form.html",context)


def log_out(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
    # return render(request,"homepage.html")


def category_view(request,category_name):
    
    category = Category.objects.get(device_category=category_name)
    devices = Device.objects.filter(device_category__device_category=category.device_category)
    
    context = {
        "devices" : devices
    }
    return render(request,"category.html",context)


def device_view(request,device_id):

    device = Device.objects.get(pk=device_id)
    device_id = device.pk
    
    context = {
        "d" : device
    }
    return render(request,'device_info.html',context)


def rangoli(request):
    categories = Category.objects.all()
    user = request.user
    machine = Heavy_machine.objects.all()
    context = {
        "machine" : machine,
        "user": user,
        "categories": categories
    }
    return render(request, 'rangoli.html', context) 


def about_us(request):
    return render(request,'aboutus.html')


def contact_us(request):
    return render(request,'contactus.html')



# @login_required
def add_to_cart(request,device_id):

    if request.user.is_authenticated:
        device = Device.objects.get(pk=device_id)
        cart = request.user.cart
        user = request.user
        
        cart.device.add(device)
        cart.save()
        
        return HttpResponseRedirect(reverse('device_view',args=(device_id,)))
    
    else :
        return HttpResponseRedirect(reverse('log_in'))


def buy(request,user_id):
    
    if request.method == 'POST':
        address = request.POST["address"]
        user = request.user
        user.address = address
        
        user.save()
        
        mail = user.email
        
        try:
            sendemail = EmailMessage(
            'Hello',
            'Body goes here',
            '2018csbha052@ldce.ac.in',
            [mail],
            ['bcc@example.com'],
            # attachments="xyz.txt",
            reply_to=['bhavysoni14@gmail.com'],
            headers={'Message-ID': 'foo'},
            )
            # sendemail.attach('mahadev',file_data,'image/jpg')
            sendemail.send()
        
        except Exception as e:
            print(e)
        # send_mail("about order","order accepted","2018csbha052@ldce.ac.in",[mail])
        
        return HttpResponse("your order is placed and mail is sent to provided mail address")


def view_cart(request):
    
    if request.user.is_authenticated:
        cart = request.user.cart
        devices = cart.device.all()
        
        context = {
            "devices" : devices
        }
    
    return render(request,"carts.html",context)
