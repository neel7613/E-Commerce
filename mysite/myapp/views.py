from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404, JsonResponse
from django.shortcuts import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *
from .models import Category,Device,Cart
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


        # categories =  list(Category.objects.all().values_list('device_category',flat=True))
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
def logged_in(request,user_id):

    # username = None
    if request.user.is_authenticated:
        username = request.user.email
        context = {
            "username" : username,
            "categories" : Category.objects.all()
        }
        # print( Device.objects.value_list("device_info",flat=True))

    # user = User.objects.all(pk=user_id)
    # username = user.username
        return render(request,"logged_in.html",context)
def homepage(request):
    user = False
    if request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('logged_in',args=(request.user.pk,)))
        user = request.user

    devices = Device.objects.all()
    categories = Category.objects.all()
    if 'search' in request.GET:
        devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
    context = {
        "categories" : categories,
        "devices" : devices,
        "user" : user
    }
    return render(request,"homepage.html",context)
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        # print("locha")
        if form.is_valid():
            # user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username = username , password = password)
            if user is not None :
                login(request,user)
                context = {
                    "username" : username
                }
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('blog-home'))

                return HttpResponseRedirect(reverse('logged_in',args=(user.pk,)),context)



            else:
                messages.error(request,'username or password not correct')
                return redirect('log_in')

                # context = {
                #         "form" : form
                # }
                # return render(request,"login_form.html",context)
            # user_id = user.id
            # username = request.user.username

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
        # with open('C:\\Users\BHAVYA\Downloads\mahadev.jpg','rb') as f:
        #     file_data = f.read()
        #     file_type = "jpg"
        #     file_name = f.name
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
        # print(devices)
        context = {
            "devices" : devices
        }
    return render(request,"carts.html",context)
