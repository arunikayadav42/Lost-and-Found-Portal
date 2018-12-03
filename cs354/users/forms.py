from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    
    #to remove unwanted text from the user form fields
    #
    first_name = forms.CharField(label=("First Name"), max_length=30,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                      'required': 'true',
                                                      'placeholder': 'First Name'}))

    last_name = forms.CharField(label=("Last Name"), max_length=30,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                      'required': 'true',
                                                      'placeholder': 'Last Name'}))

    username = forms.RegexField(label=("Username"), max_length=30, regex=r"^[\w.@+-]+$",
                                help_text=(""),
                                error_messages={'invalid': ("This value may co\
                                ntain only letters, numbers and " "@/./+/-/_ ch\
                                aracters.")},
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'required': 'true',
                                                              'placeholder': 'Username'}))
    email = forms.CharField(label=("Email"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Email'}))
    
    password1 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput(attrs={'class': 
                                                                  'form-control',
                                                                  'required': '\
                                                                   true', }))

    password2 = forms.CharField(label=("Password confirmation"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'type': 'password',
                                                                  'required': 'true',}),
                                help_text=(""),
                                error_messages={'invalid': ('Enter the same password as above')})

    roll_no = forms.RegexField(label=("Roll Number"), regex=r"^[\w.@+-]+$",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Roll',
                                                             'required': 'true'}))
    
    contact = forms.CharField(label=("Contact"), max_length=30,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Contact'}))

    addressline1 = forms.CharField(label=("Address Line 1"), max_length=30,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Address'}))

    addressline2 = forms.CharField(label=("Address Line 2"), max_length=30,
                                   required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Address2'}))

    picture = forms.FileField(required=False,)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'roll_no', 'email', 'contact', 'addressline1', 'addressline2', 'picture')


class CustomUserChangeForm(UserChangeForm):
    password = None

    first_name = forms.CharField(label=("First Name"), max_length=30,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                      'required': 'true',
                                                      'placeholder': 'First Name'}))

    last_name = forms.CharField(label=("Last Name"), max_length=30,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                      'required': 'true',
                                                      'placeholder': 'Last Name'}))

    # username = forms.RegexField(label=("Username"), max_length=30, regex=r"^[\w.@+-]+$",
    #                             help_text=(""),
    #                             error_messages={'invalid': ("This value may co\
    #                             ntain only letters, numbers and " "@/./+/-/_ ch\
    #                             aracters.")},
    #                             widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                           'required': 'true',
    #                                                           'placeholder': 'Username'}))

    email = forms.CharField(label=("Email"), max_length=30,
                            help_text=(""),
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Email'}))

    roll_no = forms.RegexField(label=("Roll Number"), regex=r"^[\w.@+-]+$",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Roll',
                                                             'required': 'true'}))

    contact = forms.CharField(label=("Contact"), max_length=30,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Contact'}))

    addressline1 = forms.CharField(label=("Address Line 1"), max_length=30,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'required': 'true',
                                                          'placeholder': 'Address'}))

    addressline2 = forms.CharField(label=("Address Line 2"), max_length=30,
                                   required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Address2'}))
    picture = forms.FileField(required=False,)
    
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        
        fields = ('first_name', 'last_name', 'email', 'roll_no', 'contact', 'addressline1', 'addressline2', 'picture')