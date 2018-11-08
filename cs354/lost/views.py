from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DateTimePickerInput
from django.urls import reverse_lazy
from .models import Lost, Comment
from .forms import CommentForm


class LostListView(ListView):
    model = Lost
    template_name = "lost/home.html"


class LostDetailView(DetailView):
    model = Lost
    template_name = "lost/detail.html"


class LostCreateView(CreateView):
    model = Lost
    fields = '__all__'
    template_name = "lost/create.html"
    def get_form(self):
        form = super().get_form()
        form.fields['date_item_lost'].widget = DateTimePickerInput()
        return form
    success_url = reverse_lazy("lost_list")


class LostUpdateView(UpdateView):
    model = Lost
    template_name = "lost/update.html"
    fields = ['title', 'description']
    

class LostDeleteView(DeleteView):
    model = Lost
    template_name = "lost/delete.html"
    success_url = reverse_lazy("lost_list")


def add_comment_to_lost(request, pk):
    lost = get_object_or_404(Lost, pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.lost = lost
        comment.save()
        return redirect('lost_detail', pk=lost.pk)
    else:
        form = CommentForm()
    return render(request, 'lost/add_comment_to_lost.html', {'form': form})