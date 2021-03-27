from rest_framework import views
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, get_object_or_404
from . import services
from . import serializers
from . import swagger_schemas as schemas
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .forms import UserAddressForm, ChangePassword
from allauth.account.views import PasswordChangeView
from .tasks import hard_task
from .serializers import UserSerializer
from rest_framework.response import Response

User = get_user_model()


class UserProfileView(DetailView):
    template_name = 'userprofile/index.html'

    def get_queryset(self):
        hard_task.delay(10)
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')

    def get_context_data(self, **kwargs):
        context = {
            'profile': self.get_object(),
            'address_form': UserAddressForm(),
            'change_password_form': ChangePassword(user=self.get_object())
        }

        return context


class UserAddressView(CreateView):

    template_name = 'userprofile/index.html'

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        print(user)
        print(kwargs)
        print(request.POST)
        form = UserAddressForm(data=request.POST, )
        if form.is_valid():
            form.save()
        print(form.errors)
        return redirect('profile:profile', pk=kwargs.get('pk'))

    def get_queryset(self):
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data['user'] = self.get_object()
        return data


class ChangePasswordView(PasswordChangeView):
    #template_name = "account/password_change." + app_settings.TEMPLATE_EXTENSION
    form_class = ChangePassword

    def get_success_url(self):
        return reverse_lazy('profile:profile', kwargs={'pk': self.kwargs.get('pk')})


class UserView(GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().select_related('profile_set').prefetch_related('profile_set__address_set')

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), id=self.request.user.id)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def get(self, request):
        object = self.get_object()
        serializer = self.get_serializer(object)
        return Response(data=serializer.data)


class AllUserView(UserView):
    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)