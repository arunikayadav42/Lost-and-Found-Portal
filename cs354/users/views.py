from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, DetailView
from django.urls import reverse_lazy
from .forms import  CustomUserCreationForm, CustomUserChangeForm
# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfile(FormView):
    template_name = 'users/userprofile.html'
    form_class = CustomUserCreationForm


class UserDetailView()
    
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('userprofile')

    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/editprofile.html', args)
    return redirect('userprofile')

