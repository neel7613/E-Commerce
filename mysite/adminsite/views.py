from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Device, Heavy_machine, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import  Q
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# def adminSearch(request):
#     if 'search' in request.GET:
#         devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
#     context = {
#         "devices" : devices
#     }
#     return render(request,"device list.html",context)
class PostListView(ListView):
    model = Device
    template_name = 'blog/devices list.html' # <app>/<model>_<viewType>.html
    context_object_name = 'devices'
    
    def test(self):
            
        if self.request.user.is_superuser:
            def get(self,request,*args,**kwargs):
                super().get(request,*args,**kwargs)
                self.object_list = self.get_queryset()
                context = self.get_context_data()
                if 'search' in request.GET:
                    devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
                    context["devices"] = devices
                return render(request,self.template_name,context)
        
        else:
            messages.success(request, f'You are not authorized to make post')
            return redirect('blog-homepage')

class PostDetailView(DetailView):
    model = Device
    template_name = 'blog/device_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class PostCreateView(CreateView):
    model = Device
    fields = ['device_category', 'device_name','device_info', 'device_price' , 'im' , 'count']
    template_name = 'blog/device_form.html'
    # def form_valid(self, form):
    #     form.instance. = self.request.user
    #     return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Device
    fields = ['device_category', 'device_name','device_info', 'device_price' , 'im' , 'count']
    template_name = 'blog/device_form.html'
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

class PostDeleteView(DeleteView):
    model = Device
    success_url = '/super'
    template_name = 'blog/device_confirm_delete.html'



class HeavyMachineDetailView(DetailView):
    model = Heavy_machine
    template_name = 'blog/HeavyMachine_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class HeavyMachineListView(ListView):
    model = Heavy_machine
    template_name = 'blog/HeavyMachine.html' # <app>/<model>_<viewType>.html
    context_object_name = 'HeavyDevices'
    
    def test(self):
            
        if self.request.user.is_superuser:
            def get(self,request,*args,**kwargs):
                super().get(request,*args,**kwargs)
                self.object_list = self.get_queryset()
                context = self.get_context_data()
                #if 'search' in request.GET:
                #    devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
                #    context["devices"] = devices
                #return render(request,self.template_name,context)
        
        else:
            messages.success(request, f'You are not authorized to make post')
            return redirect('blog-homepage')

class HeavyMachineCreateView(CreateView):
    model = Heavy_machine
    fields = ['machine_name', 'chassis','batch_capacity', 'power' , 'mixing_drum' , 'speed', 'drive', 'wire_rope', 'image']
    template_name = 'blog/HeavyMachine_form.html'
    # def form_valid(self, form):
    #     form.instance. = self.request.user
    #     return super().form_valid(form)


class HeavyMachineUpdateView(UpdateView):
    model = Heavy_machine
    fields = ['machine_name', 'chassis','batch_capacity', 'power' , 'mixing_drum' , 'speed', 'drive', 'wire_rope', 'image']
    template_name = 'blog/HeavyMachine_form.html'


class HeavyMachineDeleteView(DeleteView):
    model = Heavy_machine
    success_url = '/rangoli'
    template_name = 'blog/HeavyMachine_delete.html'



class CategoryCreateView(CreateView):
    model = Category
    fields = ['device_category', 'device_size', 'category_slug']
    template_name = 'blog/Category_form.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html' # <app>/<model>_<viewType>.html
    context_object_name = 'categories'
    
    def test(self):
            
        if self.request.user.is_superuser:
            
            def get(self,request,*args,**kwargs):
                
                super().get(request,*args,**kwargs)
                self.object_list = self.get_queryset()
                context = self.get_context_data()

                return render(request, self.template_name, context)