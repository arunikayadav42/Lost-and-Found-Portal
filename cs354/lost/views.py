from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DateTimePickerInput
from django.urls import reverse_lazy
from .models import Lost, Comment
from django.core.exceptions import PermissionDenied
from .forms import CommentForm, ItemCreateForm, ItemEditForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect


class LostListView(ListView):
    model = Lost
    template_name = "lost/home.html"


class LostDetailView(DetailView):
    model = Lost
    template_name = "lost/detail.html"


class LostCreateView(LoginRequiredMixin, CreateView):
    model = Lost
    form_class = ItemCreateForm
    template_name = "lost/create.html"
    login_url = 'login'
    success_url = reverse_lazy("lost_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields['date_item_lost'].widget = DateTimePickerInput()
        return form    


class LostUpdateView(LoginRequiredMixin, UpdateView):
    model = Lost
    template_name = "lost/update.html"
    form_class = ItemEditForm
    login_url = 'login'

    def get_form(self):
        form = super().get_form()
        form.fields['date_item_lost'].widget = DateTimePickerInput()
        return form

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
        

class LostDeleteView(LoginRequiredMixin, DeleteView):
    model = Lost
    template_name = "lost/delete.html"
    success_url = reverse_lazy("lost_list")
    login_url = 'login'
    fields = "__all__"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
        

def add_comment_to_lost(request, pk):
    lost = get_object_or_404(Lost, pk=pk)
    form = CommentForm(request.POST)
    login_url = 'login'

    if form.is_valid():
        comment = form.save(commit=False)
        comment.lost = lost
        comment.save()
        return redirect('lost_detail', pk=lost.pk)
    else:
        form = CommentForm()
    return render(request, 'lost/add_comment_to_lost.html', {'form': form})