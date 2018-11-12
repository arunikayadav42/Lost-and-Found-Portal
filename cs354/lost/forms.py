from .models import Comment, Lost
from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]