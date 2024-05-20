from django.urls import path
from .views import ShopPageView, ShopDetailsView, CartPageView

urlpatterns = [
    path('shop/', ShopPageView.as_view(), name="shop"),
    path('shop-detail/<slug:slug>', ShopDetailsView.as_view(), name="product-detail"),
    path('card/', CartPageView.as_view(), name="card"),
]