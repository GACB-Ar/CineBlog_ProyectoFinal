from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class RegisterUserForm(UserCreationForm):
    TYPE_CHOICES = (
        ('Visitor', 'Visitor'),
        ('Collaborator', 'Collaborator'),
    )

    email = forms.EmailField(label='email', required=True)
    first_name = forms.CharField(label='first_name', required=True)
    last_name = forms.CharField(label='last_name', required=True)
    username = forms.CharField(label='username', required=True)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='confirm_password', widget=forms.PasswordInput, required=True)
    profile_pic = forms.ImageField(label='profile_pic', required=False)
    user_type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select, initial='Visitor')

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'profile_pic',
            'user_type',
        )
