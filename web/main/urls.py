from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # path('', login_required(RedirectView.as_view(pattern_name='admin:index'))),
    path('', views.BaseView.as_view(), name='base'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', views.UserSignInView.as_view(), name='login'),
    # path('email/', views.SendEmailView.as_view(), name='login'),
]
