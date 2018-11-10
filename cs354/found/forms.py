from .models import Comment, Found
from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text', ]