from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from .views import (CountryAPIViewSet, CityAPIViewSet, SubCategoryAPIViewSet, ProductAPIViewSet,
                    ReviewAPIViewSet, CustomerAPIViewSet, OrderAPIViewSet, OrderItemsAPIViewSet,
                    DeliveryAddressAPIViewSet)
from rest_framework.authtoken import views

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        default_version='v1',
        description="Demo Music API",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='diyorbek@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)


router = DefaultRouter()
router.register('country', CountryAPIViewSet)
router.register('city', CityAPIViewSet)
router.register('subcategory', SubCategoryAPIViewSet)
router.register('product', ProductAPIViewSet)
router.register('review', ReviewAPIViewSet)
router.register('customer', CustomerAPIViewSet)
router.register('order', OrderAPIViewSet)
router.register('order-items', OrderItemsAPIViewSet)
router.register('delivery-address', DeliveryAddressAPIViewSet)


urlpatterns = [
    path('', include(router.urls), name='api'),
    path('auth/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
]