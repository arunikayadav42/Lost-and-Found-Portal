from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DateTimePickerInput
from django.urls import reverse_lazy
from .models import Lost, Comment
from django.core.exceptions import PermissionDenied
from .forms import CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect


class LostListView(ListView):
    model = Lost
    template_name = "lost/home.html"


# class LostDetailView(DetailView):
#     model = Lost 
#     template_name = "lost/detail.html"

#     def 


class LostCreateView(LoginRequiredMixin, CreateView):
    model = Lost
    fields = ('title', 'description', 'location', 'date_item_lost', 
              'picture')
    template_name = "lost/create.html"
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields['date_item_lost'].widget = DateTimePickerInput()
        return form

    success_url = reverse_lazy("lost_list")


class LostUpdateView(LoginRequiredMixin, UpdateView):
    model = Lost
    template_name = "lost/update.html"
    fields = ('title', 'color', 'brand', 'location', 'date_item_lost', 'picture')
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


def LostDetail(request, pk):
    lost = get_object_or_404(Lost, id=pk)
    comments = Comment.objects.filter(lost=lost, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(lost=lost, author=request.user, text=text, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(lost.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'lost': lost,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'lost/detail.html', context)