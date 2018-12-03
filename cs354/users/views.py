from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


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


