from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DateTimePickerInput
from django.urls import reverse_lazy
from .models import Found, Comment
from lost.models import Lost
from django.core.exceptions import PermissionDenied
from .forms import ItemCreateForm, ItemEditForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages


class FoundListView(ListView):
    model = Found
    template_name = "found/home.html"
    paginate_by = 5

    def get_queryset(self):
        try:
            a = self.request.GET.get('q')
        except KeyError:
            a = None
        if a:
            found_list = Found.objects.filter(
                Q(title__icontains=a) |
                Q(description__icontains=a) |
                Q(color__icontains=a) |
                Q(brand__icontains=a) |
                Q(location__icontains=a)
            )
        else:
            found_list = Found.objects.filter(approved=False).order_by("-id")
            Found.objects.filter(approved=True).delete()
        return found_list


class FoundCreateView(LoginRequiredMixin, CreateView):
    model = Found
    form_class = ItemCreateForm
    template_name = "found/create.html"
    login_url = 'login'
    success_url = reverse_lazy("found_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields['date_item_found'].widget = DateTimePickerInput()
        return form    


class FoundUpdateView(LoginRequiredMixin, UpdateView):
    model = Found
    template_name = "found/update.html"
    form_class = ItemEditForm
    login_url = 'login'

    def get_form(self):
        form = super().get_form()
        form.fields['date_item_found'].widget = DateTimePickerInput()
        return form

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
    fields = "__all__"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


def FoundDetail(request, pk):
    found = get_object_or_404(Found, id=pk)
    comments = Comment.objects.filter(found=found, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(found=found, author=request.user, 
                                             text=text, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(found.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'found': found,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'found/detail.html', context)


def Suggested_Items(request, pk):
    found = get_object_or_404(Found, pk=pk)
    q = None
    for word in found.title.split():
        q_aux = Q(title__icontains=word)
        q = (q_aux | q) if bool(q) else q_aux
    lost = Lost.objects.filter(q)

    context = {
            'lost': lost,
            'found': found,
        }

    return render(request, 'found/suggested_items.html', context)


def claim_the_item(request, pk):
    item = get_object_or_404(Found, id=pk)
    if not item.claimed_user: 
        item.claimed_user = request.user.username
        item.save()
    else:
        messages.info(request, 'Item Already Claimed', extra_tags='alert') 
        return HttpResponseRedirect(item.get_absolute_url())
    return HttpResponseRedirect(reverse_lazy("found_list"))


def claim_approved(request, pk):
    item = get_object_or_404(Found, id=pk)
    if item.claimed_user:
        item.approved = True
        item.save()
    return HttpResponseRedirect(reverse_lazy("found_list"))