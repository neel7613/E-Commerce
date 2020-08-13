from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.
machine_size_choices = (
("1","small"),
("2","medium"),
("3","large"),
)
class Category(models.Model):
    device_category = models.CharField(max_length = 200)                            # laptop,mobile,tab,ipad,PC
    device_size = models.CharField(max_length=10 , choices = machine_size_choices) # mobile-small,tab-medium,laptop-large
    category_slug = models.SlugField(unique=True)                  # this-is-mobile-collection

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.device_category

class Device(models.Model):
    device_category = models.ForeignKey(Category,max_length = 200,default =1,verbose_name = "Category",on_delete = models.SET_DEFAULT)                             #
    device_name = models.CharField(max_length = 100)
    device_info = models.TextField(help_text='Device information')
    device_price = models.CharField(max_length = 100)
    im = models.ImageField(default = "default.jpeg",upload_to="dev_im/",null=True,blank=True)
    count = models.PositiveIntegerField(null=True,blank=True)
    # device_slug = models.SlugField()


    class Meta:
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.device_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Manager(BaseUserManager):
    def create_user(self,email,password,**extra):
        user = self.model(email=email,**extra)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra)


class ExtendedUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=60,default=None,null = True,blank=True)
    # cart = models.ManyToManyField(Device)
    address = models.TextField(null = True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # REQUIRED_FIELDS = ('address',)
    USERNAME_FIELD = 'email'

    object = Manager()

    class Meta:
        verbose_name_plural = 'users'

class Cart(models.Model):
    user = models.OneToOneField(ExtendedUser,on_delete=models.CASCADE,default = 0)
    device = models.ManyToManyField(Device)
    # device_category = models.ForeignKey(Category,max_length = 200,default =1,verbose_name = "Category",on_delete = models.SET_DEFAULT)                             #
    # device_name = models.CharField(max_length = 100)
    # device_info = models.TextField()
    # device_price = models.CharField(max_length = 100)
    # im = models.ImageField(upload_to="dev_im/",null=True,blank=True)


def create_cart(sender,instance,created,**kwargs):
    if created:
        Cart.objects.create(user = instance)

post_save.connect(create_cart,sender=ExtendedUser)

# def update_cart(sender,instance,created,**kwargs):
#     if created == False:
#         Cart.objects.save(user = instance)

# post_save.connect(update_cart,sender=ExtendedUser)

class Heavy_machine(models.Model):
    machine_name = models.CharField(max_length = 100 , default=None)
    chassis = models.CharField(max_length = 300)
    batch_capacity = models.CharField(max_length = 300)
    power = models.CharField(max_length = 300)
    mixing_drum = models.CharField(max_length = 300, null=True,blank=True)
    speed = models.CharField(max_length = 300, null=True,blank=True)
    drive = models.CharField(max_length = 300, null=True,blank=True)
    wire_rope = models.CharField(max_length = 300, null=True,blank=True)
    image = models.ImageField(default = "default.jpeg",upload_to="machine/",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Heavy Machines"

    def __str__(self):
        return self.machine_name