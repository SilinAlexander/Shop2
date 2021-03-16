from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, View
from allauth.account.views import SignupView, LoginView
from django.core.mail import send_mail
from .forms import UserSignInForm, UserSignupForm
from product.models import Product


class UserSignUpView(SignupView):

   form_class = UserSignupForm
   template_name = 'account/signup.html'


class UserSignInView(LoginView):

   form_class = UserSignInForm
   template_name = 'account/login2.html'


class SendEmailView(View):

    def get(self, request, **kwargs):
        subject = 'Hello'
        message = 'Alexander'
        recipients = (
            'alexsilin1997@gmail.com',
            # 'bandirom@ukr.net'

        )
        email_from='alexsilin1997@gmail.com'
        send_mail(subject=subject, message=message, recipient_list=recipients, from_email=email_from)
        return render(request, template_name='base.html')


class BaseView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products,
            # 'cart': self.cart
        }
        print(args) #['t', 1, 100]
        print(kwargs)#{'subject': subject, 'recipient_list': recipients}
        return render(request, 'index.html', context)