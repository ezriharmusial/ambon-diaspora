from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profiel


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.'
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.'
    )
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.'
    )
    birth_date = forms.DateField(
        help_text='Required. Format: YYYY-MM-DD'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'birth_date',
            'email',
            'password1',
            'password2',
        )


class ProfielForm(forms.Modelform):
    class Meta:
        model = Profiel
        fields = (
            'username',
            'first_name',
            'last_name',
            'birth_date',
            'email',
        )
