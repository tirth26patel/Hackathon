from django.db import models

# Create your models here.
from django.db import models

class register(models.Model):
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=18)
    # photo = models.FileField(null = True, blank = True, upload_to="images/",default="")

class login (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=18)

class scheme(models.Model):
    scheme_neme = models.CharField(max_length=50,default="")
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=19)
    dob = models.DateField(null = True, blank = True,)
    password = models.CharField(max_length=20, default=None)
    gender = models.CharField(max_length=6,default="2")
    Aadhar = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Pancard = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Incomecerti = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Castcerti = models.FileField(null = True, blank = True, upload_to="images/",default="")
    photo = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Birthcerti = models.FileField(null = True, blank = True, upload_to="images/",default="")
    sign = models.FileField(null = True, blank = True, upload_to="images/",default="")
    educationalCerti = models.FileField(null = True, blank = True, upload_to="images/",default="")

from django import forms
from home.models import scheme
class schemeForm(forms.ModelForm):
    class Meta:
        model = scheme
        fields = ['FirstName','MiddleName','LastName','Email','phone','password','Aadhar','Pancard','Incomecerti','Castcerti','photo','Birthcerti']

class scholarship(models.Model):
    scholarship_name = models.CharField(max_length=50,default="")
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=19)
    dob = models.DateField(null = True, blank = True,)
    gender = models.CharField(max_length=6,default="2")
    ac_name = models.CharField(max_length=50)
    ac_no = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=50)
    Aadhar = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Pancard = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Incomecerti = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Castcerti = models.FileField(null = True, blank = True, upload_to="images/",default="")
    photo = models.FileField(null = True, blank = True, upload_to="images/",default="")
    Birthcerti = models.FileField(null = True, blank = True, upload_to="images/",default="")
    sign = models.FileField(null = True, blank = True, upload_to="images/",default="")
    educationalCerti = models.FileField(null = True, blank = True, upload_to="images/",default="")