from django.urls import path
from .views import *


urlpatterns = [
    path('super/', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('heavymachine/create', HeavyMachineCreateView.as_view(), name="HeavyMachine-create"),
    path('heavymachine/<int:pk>', HeavyMachineDetailView.as_view(), name="HeavyMachine-detail"),
    path('heavymachine/<int:pk>/update/', HeavyMachineUpdateView.as_view(), name="HeavyMachine-update"),
    path('heavymachine/<int:pk>/delete/', HeavyMachineDeleteView.as_view(), name="HeavyMachine-delete"),
    path('category/create', CategoryCreateView.as_view(), name="category-create"),
	path('category/list',CategoryListView.as_view(),name="category-list"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name="category-delete"),


    # path('about/', views.about, name="blog-about")
]
