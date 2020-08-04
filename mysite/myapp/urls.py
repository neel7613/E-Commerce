from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name = "homepage"),
    path('register/',views.register,name = "register"),
    path('<int:user_id>/',views.logged_in,name = "logged_in"),
    path('login/',views.log_in,name = "log_in"),
    path('logout/',views.log_out,name = "log_out"),
    path('<slug:single_slug>/',views.single_slug,name="single_slug"),
    path('device/<int:device_id>/',views.device_view,name="device_view"),
    path('your-cart/<int:device_id>/',views.add_to_cart,name = "add_to_cart"),
    path('placed-order/<int:user_id>/',views.buy,name = "buy")
]
