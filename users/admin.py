from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Locality, School, CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'first_name', 'last_name', 'school', 'mob_parent', 'mob_student', 'locality']
    model = CustomUser

admin.site.register(Locality)
admin.site.register(School)
admin.site.register(CustomUser, CustomUserAdmin)
