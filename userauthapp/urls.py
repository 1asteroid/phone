from django.urls import path
from .views import UserLoginView, UserRegisterView, UserLogOutView


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name='register'),
    path("accounts/login/", UserLoginView.as_view(), name='login'),
    path("logout/", UserLogOutView.as_view(), name='logout'),
]