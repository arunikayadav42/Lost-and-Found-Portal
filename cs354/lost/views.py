from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DateTimePickerInput
from django.urls import reverse_lazy
from .models import Lost, Comment
from found.models import Found
from django.core.exceptions import PermissionDenied
from .forms import ItemCreateForm, ItemEditForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.db.models import Max
from users.models import CustomUser
<<<<<<< HEAD
=======

>>>>>>> Links for comments working

class LostListView(ListView):
    template_name = "lost/home.html"
    model = Lost
    paginate_by = 2
    
    def get_queryset(self):
        try:
            a = self.request.GET.get('q')
        except KeyError:
            a = None
        if a:
            lost_list = Lost.objects.filter(
                Q(title__icontains=a) |
                Q(description__icontains=a) |
                Q(color__icontains=a) |
                Q(brand__icontains=a) |
                Q(location__icontains=a)
            )
        else:
            lost_list = Lost.objects.order_by("-id")
        return lost_list
        

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


def Suggested_Items(request, pk):
    lost = get_object_or_404(Lost, pk=pk)
    q = None
    for word in lost.title.split():
        q_aux = Q(title__icontains=word)
        q = (q_aux | q) if bool(q) else q_aux
    found = Found.objects.filter(q).filter(claimed_user=None)

    context = {
            'lost': lost,
            'found': found,
        }

    return render(request, 'lost/suggested_items.html', context)


def item_found(request, pk): 
    item = Lost.objects.get(id=pk)
    if not item.claimed_user:
        item.item_found = True
        item.claimed_user = request.user.username
        item.save()

    return HttpResponseRedirect(reverse_lazy("lost_list")) 


def item_claimed(request, pk):
    item = Lost.objects.get(id=pk)
    Lost.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse_lazy("lost_list"))
