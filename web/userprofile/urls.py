from .views import UserProfileView, UserAddressView, ChangePasswordView
from django.urls import path
app_name = 'profile'


urlpatterns = [
    path('<pk>/', UserProfileView.as_view(), name='profile'),
    path('<pk>/address/', UserAddressView.as_view(), name='user_address'),
    path('<pk>/change_password/', ChangePasswordView.as_view(), name='change_password'),

]