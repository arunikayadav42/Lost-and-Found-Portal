from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Found, Comment
from .forms import CommentForm


class FoundListView(ListView):
    model = Found
    template_name = "found/home.html"


class FoundDetailView(DetailView):
    model = Found
    template_name = "found/detail.html"


class FoundCreateView(CreateView):
    model = Found
    template_name = "found/create.html"
    fields = "__all__"
    success_url = reverse_lazy("found_list")


class FoundUpdateView(UpdateView):
    model = Found
    template_name = "found/update.html"
    fields = ['title', 'description']
    

class FoundDeleteView(DeleteView):
    model = Found
    template_name = "found/delete.html"
    success_url = reverse_lazy("found_list")


def add_comment_to_found(request, pk):
    found = get_object_or_404(Found, pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.found = found
        comment.save()
        return redirect('found_detail', pk=found.pk)
    else:
        form = CommentForm()
    return render(request, 'found/add_comment_to_found.html', {'form': form})