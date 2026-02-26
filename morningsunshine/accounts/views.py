from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render

#i just want this somewhere so its here now
ROLES = [
    ("role_3", "Admin"),
    ("role_0", "Voice"),
    ("role_1", "Cyberspace"),
    ("role_2", "Temperance"),
]
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def profile(request):
    return render(request,"accounts/myspace.html")
