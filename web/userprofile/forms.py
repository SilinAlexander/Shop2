from allauth.account.forms import SetPasswordForm, ChangePasswordForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from .models import Address
from django_countries.widgets import CountrySelectWidget


class UserAddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.user = kwargs.get('user')
        # print(self.user)

    city = forms.CharField(widget=forms.TextInput({
        'placeholder': 'city',
        'class': 'form-control'
    }))

    region = forms.CharField(widget=forms.TextInput({
        'placeholder': 'region',
        'class': 'form-control'
    }))

    street = forms.CharField(widget=forms.TextInput({
        'placeholder': 'street',
        'class': 'form-control'
    }))

    index = forms.CharField(widget=forms.TextInput({
        'placeholder': 'index',
        'class': 'form-control'
    }))

    recipient = forms.CharField(widget=forms.TextInput({
        'placeholder': 'recipient',
        'class': 'form-control'
    }))

    class Meta:
        model = Address
        exclude = ('profile', )
        widgets = {'country': CountrySelectWidget()}

    def save(self, commit=True):
        # self.cleaned_data['profile'] = self.user.profile_set
        self.cleaned_data['profile_id'] = self.initial['profile_id']
        print(self.cleaned_data)
        return Address.objects.create(**self.cleaned_data)


class ChangePassword(ChangePasswordForm):
    pass
