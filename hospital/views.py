from distutils.log import error
from struct import pack
from threading import local
from django.shortcuts import render,redirect
from . models import Appointment, Contact, Doctor, Patient
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

def admin_logout(request):
    logout(request)
    return redirect('index')

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all().count()
    patient = Patient.objects.all().count()
    appointment = Appointment.objects.all().count()
    context = {'doctor':doctor,'patient':patient,'appointment':appointment}
    return render(request,'admin_home.html',context)    

def add_doctor(request):
    error = ""
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        special = request.POST['special']
        try:
            Doctor.objects.create(name=name,mobile=mobile,special=special)
            error = "no"
        except:
            error = "yes"
    return render(request,'add_doctor.html',locals())

def view_doctor(request):
    if not request.user.is_authenticated:
        return redirect('login')
    doctors = Doctor.objects.all()        
    context = { 'doctors':doctors }
    return render(request,'view_doctor.html',locals())

def delete_doctor(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('view_doctor')

def edit_doctor(request,id):
    error = ""            
    if not request.user.is_authenticated:
            return redirect('login')    
    doctor = Doctor.objects.get(id=id)            
    
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        special = request.POST['special']       
    try:
        doctor.name = name
        doctor.mobile = mobile
        doctor.special = special
        doctor.save()
        error = "no"
    except:
        error = "yes"   
    return render(request,'edit_doctor.html',locals())         

def add_patient(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']
        try:
            Patient.objects.create(name=name,gender=gender,mobile=mobile)
            error = "no"
        except:
            error = "yes"
    return render(request,'add_patient.html',locals())

def view_patient(request):
    if not request.user.is_authenticated:
        return redirect('login')
    patients = Patient.objects.all()
    return render(request,'view_patient.html',locals())

def delete_patient(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    patient = Patient.objects.get(id=id)    
    patient.delete()
    return redirect('view_patient')

def edit_patient(request,id):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')    
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        address = request.POST['address']

        patient.name = name
        patient.mobile = mobile
        patient.gender = gender
        patient.address = address

        try:
            patient.save()
            error = "no"
        except:
            error = "yes"

    return render(request,'edit_patient.html',locals())

def unread_queries(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')  
    unreads = Contact.objects.filter(is_read="no")    
    return render(request,'unread_queries.html',locals())    

def read_queries(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')          
    reads = Contact.objects.filter(is_read="yes")
    return render(request,'read_queries.html',locals())

def view_queries(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    queries = Contact.objects.get(id=id)    
    queries.is_read = "yes"
    queries.save()
    return render(request,'view_queries.html',locals())

def add_appointment(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == "POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        date1 = request.POST['date']
        time1 = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()      
        try:
            Appointment.objects.create(doctor=doctor,
                                        patient=patient,
                                        date=date1,
                                        time=time1)

            error = "no"
        except:
            error = "yes" 
    context = {
        'doctor':doctor1,
        'patient':patient1,
        'error':error
    }
    return render(request,'add_appointment.html',context)

def delete_appointment(request,id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('view_appointment')

def view_appointment(request):
    appointments = Appointment.objects.all()
    context = {
        'appointments':appointments
    }
    return render(request,'view_appointment.html',context)

