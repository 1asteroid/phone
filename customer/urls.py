from django.urls import path
from .views import ShopPageView, ShopDetailsView, CartPageView, update_item, CheckOutView

urlpatterns = [
    path('shop/', ShopPageView.as_view(), name="shop"),
    path('shop-detail/<slug:slug>', ShopDetailsView.as_view(), name="shop-detail"),
    path('shop-detail/update_item/', update_item, name="shop-detail-update-item"),
    path('card/', CartPageView.as_view(), name="card"),
    path('update_item/', update_item, name="update_item"),
    path('shop/update_item/', update_item, name="shop-update-item"),
    path('card/update_item/', update_item, name="card-update-item"),
    path('checkout/', CheckOutView.as_view(), name="check-out"),
]

