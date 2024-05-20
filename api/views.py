from django.db.models import Avg
from django.db.transaction import atomic
from rest_framework.decorators import action


from .serializers import (CountrySerializer, CitySerializer, SubCategorySerializer, ProductSerializer, ReviewSerializer,
                          CustomerSerializer, OrderSerializer, OrderItemsSerializer, DeliveryAddressSerializer)
from product.models import Product, SubCategory, Review
from address.models import Country, City, DeliveryAddress
from customer.models import Customer, Order, OrderItems

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.response import Response


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )


class SubCategoryAPIViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', "category"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=["GET"])
    def count(self, request, *args, **kwargs):
        product = self.get_object()
        with atomic():
            product.view_count += 1
            product.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def cheap(self, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by("price")
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def expensive(self, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by("-price")
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)


class ReviewAPIViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['user', "product"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )


class CustomerAPIViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['user']
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )


class OrderAPIViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['user']
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )


class OrderItemsAPIViewSet(ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', "category"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )


class DeliveryAddressAPIViewSet(ModelViewSet):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name', "category"]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated, )