from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name = "homepage"),
    path('register/',views.register,name = "register"),
    path('<int:user_id>/',views.logged_in,name = "logged_in"),
    path('login/',views.log_in,name = "log_in"),
    path('logout/',views.log_out,name = "log_out"),
    path('your-cart/',views.view_cart,name = "view_cart"),
    path('<slug:single_slug>/',views.single_slug,name="single_slug"),
    path('device/<int:device_id>/',views.device_view,name="device_view"),
    path('category/<str:category_name>/',views.category_view,name="category_view"),
    path('add-to-cart/<int:device_id>/',views.add_to_cart,name = "add_to_cart"),
    path('placed-order/<int:user_id>/',views.buy,name = "buy"),
]
