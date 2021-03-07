from allauth.account.forms import SignupForm, LoginForm, PasswordField
from django import forms


class UserSignupForm(SignupForm):
    pass


class UserSignInForm(LoginForm):
    password = PasswordField(
        required=True,
        label="Password",
        # autocomplete="current-password",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',

        }))

