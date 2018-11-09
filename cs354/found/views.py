from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Found, Comment
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class FoundListView(ListView):
    model = Found
    template_name = "found/home.html"


class FoundDetailView(DetailView):
    model = Found
    template_name = "found/detail.html"


class FoundCreateView(LoginRequiredMixin, CreateView):
    model = Found
    template_name = "found/create.html"
    fields = ('title', 'description', 'location', 'date', 'picture')
    success_url = reverse_lazy("found_list")
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields['date_item_lost'].widget = DateTimePickerInput()
        return form


class FoundUpdateView(LoginRequiredMixin, UpdateView):
    model = Found
    template_name = "found/update.html"
    fields = "('title', 'description', 'location', 'date', 'picture')"
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
            

class FoundDeleteView(LoginRequiredMixin, DeleteView):
    model = Found
    template_name = "found/delete.html"
    success_url = reverse_lazy("found_list")
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
        

def add_comment_to_found(LoginRequiredMixin, request, pk):
    found = get_object_or_404(Found, pk=pk)
    form = CommentForm(request.POST)
    login_url = 'login'

    if form.is_valid():
        comment = form.save(commit=False)
        comment.found = found
        comment.save()
        return redirect('found_detail', pk=found.pk)
    else:
        form = CommentForm()
    return render(request, 'found/add_comment_to_found.html', {'form': form})