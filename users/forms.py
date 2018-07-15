from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'mob_parent', 'mob_student', 'locality', 'school', 'password1', 'password2',)

    def __generate_username(self, first_name,last_name):
        val = "{0}{1}".format(first_name[0],last_name).lower()
        x=0
        while True:
            if x == 0 and CustomUser.objects.filter(username=val).count() == 0:
                return val
            else:
                new_val = "{0}{1}".format(val,x)
                if CustomUser.objects.filter(username=new_val).count() == 0:
                    return new_val
                x += 1
                if x > 1000000:
                    raise Exception("Too many users have same name. Cannot generate username.")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.__generate_username(self.cleaned_data['first_name'],self.cleaned_data['last_name'])
        if commit:
            user.save()
        return user



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
