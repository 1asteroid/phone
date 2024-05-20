
from rest_framework.serializers import ModelSerializer
from address.models import Country, City, DeliveryAddress
from customer.models import Customer, Order, OrderItems
from product.models import Product, SubCategory, Review


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(ModelSerializer):

    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'country', 'name')


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'image')


class ProductSerializer(ModelSerializer):

    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'category', 'subcategory', 'price', 'price_type',
                  "image", 'max_count', 'color', 'size', 'description', 'view_count')


class ReviewSerializer(ModelSerializer):

    product = ProductSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'product', 'text', 'rating')


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer,
        fields = ('id', 'user', 'image')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'slug', 'date_ordered')


class OrderItemsSerializer(ModelSerializer):

    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItems
        fields = ('id', 'product', 'order', 'quantity', 'date_added')


class DeliveryAddressSerializer(ModelSerializer):

    order = OrderSerializer
    city = CitySerializer(read_only=True)

    class Meta:
        model = DeliveryAddress
        fields = ('id', 'order', 'city', 'date_added')


