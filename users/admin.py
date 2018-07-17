from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, FooBarForm
from .models import Locality, School, CustomUser

class CustomUserAdmin(admin.ModelAdmin):

    fields =  ('email', 'first_name', 'last_name', 'school', 'mob_parent', 'mob_student', 'locality')
    model = CustomUser # is this line necessary?

# For each model, optionally create a ModelAdmin class that encapsulates the customized admin functionality and options for the particular model.

admin.site.register(Locality)
admin.site.register(School)
admin.site.register(CustomUser, CustomUserAdmin)
