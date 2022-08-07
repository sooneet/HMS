from django.contrib import admin
from django.urls import path
from hospital import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('login/', views.admin_login,name='login'),
    path('admin_home/', views.admin_home,name='admin_home'),
]
