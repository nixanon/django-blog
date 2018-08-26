# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView): # pylint: disable=too-many-ancestors
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'