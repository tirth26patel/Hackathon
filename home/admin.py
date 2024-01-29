from django.contrib import admin
from home.models import register
from home.models import scheme, scholarship

# Register your models here.
class rshow(admin.ModelAdmin):
    list_display=['username','password']
admin.site.register(register,rshow)
class sshow(admin.ModelAdmin):
    list_display=['FirstName','MiddleName','LastName']
admin.site.register(scheme,sshow)

class shshow(admin.ModelAdmin):
    list_display=['MiddleName']
admin.site.register(scholarship,shshow)