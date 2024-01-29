from django.http import HttpResponse
from home.models import register
from home.models import scheme, scholarship
from django.shortcuts import render
import ctypes
# Create your views here.
def index(request):
    name = register.objects.all()
    return render(request, 'index.html',{"name":name})

def index1(request):
    render(request,'profile.html')
    return render(request,'index1.html')

def profile(request):
    return render(request,'login.html')

def profile1(request):
    return render(request,'profile1.html')

def forget(request):
    return render(request, 'forget.html')
def registration(request):  # Renamed the view function to 'registration'
    if request.method == "POST":
        username = request.POST.get('username')
        gender = request.POST.get('gender', None)
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # photo = request.FILES.get('photo')    
        new_register = register(username=username,gender=gender,phone=phone,address=address,email=email,password=password)
        new_register.save()
        
        return render(request, 'index.html')
    return render(request, 'register.html')


def adiwasi(request):
    if request.method == "POST":
        scheme_name="adiwasi-vikas-yojana"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scheme(scheme_neme=scheme_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'schemes/scheme01.html')
    return render(request, 'scheme_apply/ADIWASI-VIKAS-YOJANA.html')

def ashram(request):
    if request.method == "POST":
        scheme_name="ASHRAM-SHALA"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scheme(scheme_neme=scheme_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'schemes/scheme02.html')
    return render(request, 'scheme_apply/ASHRAM-SHALA.html')
from django.shortcuts import render
from home.models import scheme

def eklavya(request):
    if request.method == "POST":
        scheme_name="Eklavya-Model-Residential-Schools"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scheme(scheme_neme=scheme_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'schemes/scheme03.html')
    return render(request, 'scheme_apply/Eklavya-Model-Residential-Schools.html')

def tribal_d(request):
    if request.method == "POST":
        scheme_name="TRIBAL-DEVELOPMENT-SCHEMES-FOR-WOMEN"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scheme(scheme_neme=scheme_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'schemes/scheme04.html')
    return render(request, 'scheme_apply/TRIBAL-DEVELOPMENT-SCHEMES-FOR-WOMEN.html')

def tribal_y(request):
    if request.method == "POST":
        scheme_name="tribal-youth-hostel"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scheme(scheme_neme=scheme_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'schemes/scheme05.html')
    return render(request, 'scheme_apply/tribal-youth-hostel.html')

def van(request):
    if request.method == "POST":
        scheme_name="VAN-DHAN-VIKAS"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scheme(scheme_neme=scheme_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'schemes/scheme06.html')
    return render(request, 'scheme_apply/VAN-DHAN-VIKAS.html')

def vanbandhu(request):
    if request.method == "POST":
        scheme_name="VANBANDHU-KLYAN-YOJAN"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scheme(scheme_neme=scheme_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'schemes/scheme07html')
    return render(request, 'scheme_apply/VANBANDHU-KLYAN-YOJAN.html')

def login_in(request):
    if request.method == "POST":
        ch_username = request.POST.get('username')
        ch_password = request.POST.get('password')
        count=register.objects.all().count()
        for i in range(count):
            nusername = register.objects.all()[i].username
            if ch_username == nusername:
                npassword = register.objects.all()[i].password
                if npassword == ch_password:
                    nphone = register.objects.all()[i].phone
                    naddress = register.objects.all()[i].address
                    nemail = register.objects.all()[i].email
                    ngender = register.objects.all()[i].gender
                    # nphoto = register.objects.all()[i].photo
                    details = {
                        'username': nusername,
                        'phone': nphone,
                        'address':naddress,
                        'email':nemail,
                        'gender':ngender,
                        # 'photo':nphoto,   
                    }
                    # In your view function after successful login
                    if ch_username:
                        request.session['username'] = nusername  # Store the user's ID in the session
                        return render(request, 'profile1.html', details)
    return render(request,'login.html')

# In your profile view function
def profile(request):
    nusername = request.session.get('username')
    if nusername:
        count=register.objects.all().count()
        for i in range(count):
            username = register.objects.all()[i].username
            if nusername == username:
                nusername = register.objects.all()[i].username
                nphone = register.objects.all()[i].phone
                naddress = register.objects.all()[i].address
                nemail = register.objects.all()[i].email
                ngender = register.objects.all()[i].gender
                # nphoto = register.objects.all()[i].photo
                details = {
                    'username': nusername,
                    'phone': nphone,
                    'address':naddress,
                    'email':nemail,
                    'gender':ngender,
                    # 'photo':nphoto,
                }
        return render(request, 'profile1.html', details)
    else:
        return render(request, 'login.html')

def log_out(request):
    request.session['username'] = None  # Store the user's ID in the session
    return render(request,"index.html")
def gujarat(request):
    if request.method == "POST":
        scholarship_name="gujarat-state-handicapped-education"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        ac_name = request.POST.get('ac_name')
        ac_no = request.POST.get('ac_no')
        ifsc = request.POST.get('ifsc')
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scholarship(scholarship_name=scholarship_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,ac_name=ac_name,ac_no=ac_no,ifsc=ifsc,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'scholarships/scholarship1.html')
    return render(request, 'scholarship_apply/gujarat-state-handicapped-education.html')

def mukhyamantri(request):
    if request.method == "POST":
        scholarship_name="mukhyamantri-yuva-swavalamban-yojana"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        ac_name = request.POST.get('ac_name')
        ac_no = request.POST.get('ac_no')
        ifsc = request.POST.get('ifsc')
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scholarship(scholarship_name=scholarship_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,ac_name=ac_name,ac_no=ac_no,ifsc=ifsc,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'scholarships/scholarship1.html')
    return render(request, 'scholarship_apply/mukhyamantri-yuva-swavalamban-yojana.html')

def national_over(request):
    if request.method == "POST":
        scholarship_name="national-overseas-scholarship"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        ac_name = request.POST.get('ac_name')
        ac_no = request.POST.get('ac_no')
        ifsc = request.POST.get('ifsc')
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scholarship(scholarship_name=scholarship_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,ac_name=ac_name,ac_no=ac_no,ifsc=ifsc,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'scholarships/scholarship1.html')
    return render(request, 'scholarship_apply/national-overseas-scholarship.html')

def pe_matric(request):
    if request.method == "POST":
        scholarship_name="pe-matric"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        ac_name = request.POST.get('ac_name')
        ac_no = request.POST.get('ac_no')
        ifsc = request.POST.get('ifsc')
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scholarship(scholarship_name=scholarship_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,ac_name=ac_name,ac_no=ac_no,ifsc=ifsc,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'scholarships/scholarship1.html')
    return render(request, 'scholarship_apply/pe-matric.html')

def post_matric(request):
    if request.method == "POST":
        scholarship_name="post-matric"
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob=request.POST.get('DOB')
        gender = request.POST.get('gender', None)
        ac_name = request.POST.get('ac_name')
        ac_no = request.POST.get('ac_no')
        ifsc = request.POST.get('ifsc')
        Aadhar = request.FILES.get('Aadhar')
        Pancard = request.FILES.get('Pancard')
        Incomecerti = request.FILES.get('Incomecerti')
        Castcerti = request.FILES.get('Castcerti')
        photo = request.FILES.get('photo')
        Birthcerti = request.FILES.get('Birthcerti')
        sign = request.FILES.get('Sign')
        educationalCerti = request.FILES.get('EducationalCerti')
        new_scheme = scholarship(scholarship_name=scholarship_name,FirstName=FirstName,MiddleName=MiddleName,LastName=LastName,Email=Email,phone=phone,password=password,dob=dob,gender=gender,ac_name=ac_name,ac_no=ac_no,ifsc=ifsc,Aadhar=Aadhar,Pancard=Pancard,Incomecerti=Incomecerti,Castcerti=Castcerti,photo=photo,Birthcerti=Birthcerti,sign=sign,educationalCerti=educationalCerti)
        new_scheme.save()
        return render(request, 'scholarships/scholarship1.html')
    return render(request, 'scholarship_apply/post-matric.html')

def admin_page(request):
    details=scholarship.objects.all()
    return render(request,'admin_page.html',{'details':details}) 

def admin_details(request,details):
    n_username=details
    count=scholarship.objects.all().count()
    for i in range(count):
        nusername = scholarship.objects.all()[i].FirstName
        if n_username == nusername:
            scholarship_name= scholarship.objects.all()[i].scholarship_name
            FirstName = scholarship.objects.all()[i].FirstName
            MiddleName = scholarship.objects.all()[i].MiddleName
            LastName = scholarship.objects.all()[i].LastName
            Email = scholarship.objects.all()[i].Email
            phone = scholarship.objects.all()[i].phone
            password = scholarship.objects.all()[i].password
            dob = scholarship.objects.all()[i].dob
            gender = scholarship.objects.all()[i].gender
            ac_name = scholarship.objects.all()[i].ac_name
            ac_no = scholarship.objects.all()[i].ac_no
            ifsc = scholarship.objects.all()[i].ifsc
            Aadhar = scholarship.objects.all()[i].Aadhar
            Pancard = scholarship.objects.all()[i].Pancard
            Incomecerti = scholarship.objects.all()[i].Incomecerti
            Castcerti = scholarship.objects.all()[i].Castcerti
            photo = scholarship.objects.all()[i].photo
            Birthcerti = scholarship.objects.all()[i].Birthcerti
            sign = scholarship.objects.all()[i].sign
            educationalCerti = scholarship.objects.all()[i].educationalCerti
            details = {
                        'scholarship_name':scholarship_name,'FirstName':FirstName,'MiddleName':MiddleName,'LastName':LastName,'Email':Email,'phone':phone,'password':password,'dob':dob,'gender':gender,'ac_name':ac_name,'ac_no':ac_no,
                        'ifsc':ifsc,'Aadhar':Aadhar,'Pancard':Pancard,'Incomecerti':Incomecerti,'Castcerti':Castcerti,'photo':photo,'Birthcerti':Birthcerti,'sign':sign,'educationalCerti':educationalCerti,
                    }
    return render(request,'admin_details.html',{'details':details}) 
    

def scheme01(request):
    return render(request,'schemes/scheme01.html')

##################################################
def scheme02(request):
    return render(request,'schemes/scheme02.html')
def scheme03(request):
    return render(request,'schemes/scheme03.html')
def scheme04(request):
    return render(request,'schemes/scheme04.html')
def scheme05(request):
    return render(request,'schemes/scheme05.html')
def scheme06(request):
    return render(request,'schemes/scheme06.html')
def scheme07(request):
    return render(request,'schemes/scheme07.html')
##################################################


#########################################################
def scholarship1(request):
    return render(request,'scholarships/scholarship1.html')
def scholarship2(request):
    return render(request,'scholarships/scholarship2.html')
def scholarship3(request):
    return render(request,'scholarships/scholarship3.html')
def scholarship4(request):
    return render(request,'scholarships/scholarship4.html')
def scholarship5(request):
    return render(request,'scholarships/scholarship5.html')
##########################################################


def scheme_page(request):
    return render(request,'scheme-page.html')
def scholarship_page(request):
    return render(request,'scholarship-page.html')



def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')