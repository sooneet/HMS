from django.contrib import admin
from django.urls import path
from hospital import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('login/', views.admin_login,name='login'),
    path('logout/', views.admin_logout,name='logout'),
    path('admin_home/', views.admin_home,name='admin_home'),
    path('add_doctor/', views.add_doctor,name='add_doctor'),
    path('add_patient/', views.add_patient,name='add_patient'),
    path('view_doctor/', views.view_doctor,name='view_doctor'),
    path('view_patient/', views.view_patient,name='view_patient'),
    path('delete_doctor/<int:id>/', views.delete_doctor,name='delete_doctor'),
    path('delete_patient/<int:id>/', views.delete_patient,name='delete_patient'),
    path('edit_doctor/<int:id>/', views.edit_doctor,name='edit_doctor'),
    path('edit_patient/<int:id>/', views.edit_patient,name='edit_patient'),
    path('edit_patient/<int:id>/', views.edit_patient,name='edit_patient'),
    path('unread_queries/', views.unread_queries,name='unread_queries'),
    path('read_queries/', views.read_queries,name='read_queries'),
    path('add-appointment/', views.add_appointment,name='add_appointment'),
    path('view_appointment/', views.view_appointment,name='view_appointment'),
    path('delete-appointment/<int:id>/', views.delete_appointment,name='delete_appointment'),
]
