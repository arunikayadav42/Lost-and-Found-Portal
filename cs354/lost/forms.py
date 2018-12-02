from .models import Comment, Lost
from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class CommentForm(forms.ModelForm):
	text = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment here ...', 'rows': '2', 'cols': '15'}))
	
	class Meta:
		model = Comment
		fields = ['text', ]	