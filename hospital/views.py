from django.shortcuts import render,redirect
from . models import Contact
from datetime import date
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    error = ""
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        subject = request.POST['subject']
        message  = request.POST['message']   
        try:
            Contact.objects.create(name=name,
                                    mob_no=contact,
                                    email=email,
                                    subject=subject,
                                    message=message,
                                    message_date = date.today(),
                                    is_read="no")
            error = "no"                        
        except:
            error = "yes"
    return render(request,'contact.html',locals())

def admin_login(request):
    error = ""
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pwd']
        user = authenticate(username=username,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
        except:
            error = "yes"
    return render(request,'login.html',locals())

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'admin_home.html',locals())    