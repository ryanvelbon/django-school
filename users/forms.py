from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.forms import ModelForm # new

class FooBarForm(ModelForm):
    class Meta:
        model = CustomUser
        # fields = ('first_name', 'last_name', 'email')
        exclude = ('username',)

class CustomUserCreationForm(UserCreationForm):
    """Form: http://localhost:8000/users/signup/"""

    email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'mob_parent', 'mob_student', 'locality', 'school', 'password1', 'password2',)
        # fields = UserCreationForm.Meta.fields # default fields


    # def save(self, commit=True):
    #     user = super(CustomUserCreationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.username = self.__generate_username(self.cleaned_data['first_name'],self.cleaned_data['last_name'])
    #     if commit:
    #         user.save()
    #     return user



class CustomUserChangeForm(UserChangeForm):
    """Form: http://localhost:8000/admin/users/customuser/7/change/"""

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
