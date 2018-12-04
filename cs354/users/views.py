from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def login(request):
    if request.user.is_authenticated():
        return redirect('userprofile')
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            login(request, user)
            return redirect('userprofile')
 
        else:
            messages.error(request, 'Error wrong username/password')
 
    return render(request, 'login.html')
 
 
def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')
 
 
def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('blog_login')
 
    return render(request, 'blog/admin_page.html')


class UserProfile(FormView):
    template_name = 'users/userprofile.html'
    form_class = CustomUserCreationForm


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "users/profileview.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/editprofile.html'
    success_url = reverse_lazy('userprofile')

    def get_object(self):
        return CustomUser.objects.get(username=self.request.user)