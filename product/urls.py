from django.urls import path
from .views import HomePageView, BaseView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]
