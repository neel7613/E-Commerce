from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Device
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
    # ordering = ['-date_posted']
    def get(self,request,*args,**kwargs):
        super().get(request,*args,**kwargs)
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        if 'search' in request.GET:
            devices = Device.objects.filter(Q(device_name__icontains=request.GET['search']) | Q(device_category__device_category__icontains=request.GET['search']) | Q(device_info__icontains=request.GET['search']))
            context["devices"] = devices
        return render(request,self.template_name,context)

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
