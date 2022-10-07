from django.contrib import admin
from myapp.models import signup

# Register your models here.
@admin.register(signup)
class Admin(admin.ModelAdmin):
    list_display=['id','name','email','username','password']
