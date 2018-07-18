from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import CustomUser

# Note that there is a mixture of FBVs and CBVs

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# Having failed to make a CBV DetailView, I settled for an FBV for this view.
def student_profile_view(request, username):
    student = CustomUser.objects.get(username=username)
    return render(request, 'student_profile.html', {'student': student})
