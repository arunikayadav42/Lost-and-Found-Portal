from .models import Lost, Comment
from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class ItemCreateForm(forms.ModelForm):
    title = forms.CharField(label=("Title"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'What\'s the kind of article'}))
    location = forms.CharField(label=("Location"), max_length=30,
                               help_text=(""),
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Where did you find the article'}))

    brand = forms.CharField(label=("Brand"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'What\'s the brand of the item'}))
    color = forms.CharField(label=("Color"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Describe the color of the item'}))

    description = forms.CharField(label=("Additional Description"), max_length=30,
                                  help_text=(""),
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'required': 'true',
                                                                'placeholder': 'Describe the item so that we can find it better'}))
    picture = forms.FileField()

    class Meta:
        model = Lost
        exclude = ('found_status', 'date_item_registered', 'author')


class ItemEditForm(forms.ModelForm):
    title = forms.CharField(label=("Title"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'What\'s the kind of article'}))
    location = forms.CharField(label=("Location"), max_length=30,
                               help_text=(""),
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Where did you find the article'}))

    brand = forms.CharField(label=("Brand"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'What\'s the brand of the item'}))
    color = forms.CharField(label=("Color"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Describe the color of the item'}))

    description = forms.CharField(label=("Additional Description"), max_length=30,
                                  help_text=(""),
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'required': 'true',
                                                                'placeholder': 'Describe the item so that we can find it better'}))
    class Meta:
        model = Lost
        exclude = ('found_status', 'date_item_registered', 'author')


class CommentForm(forms.ModelForm):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment here ...', 'rows': '2', 'cols': '15'}))
  
    class Meta:
        model = Comment
        fields = ['text', ]