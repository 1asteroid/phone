from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Avg

import json
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product, SubCategory, Review
from customer.models import Order, OrderItems
from address.models import City, DeliveryAddress
from django.views.decorators.csrf import csrf_exempt


def count_item_product(request):
    user = request.user
    order = Order.objects.get(user=user)
    order_items = OrderItems.objects.filter(order=order)
    return order_items.count()


class ShopPageView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        subcategories = SubCategory.objects.all()

        name = request.GET.get('name')
        category = request.GET.get('category')


        if category:
            products = products.filter(category_icontains=category)

        if name:
            products = products.filter(name__icontains=name)

        context = {
            "products": products,
            "subcategories": subcategories,
            'items_count': count_item_product(request)
        }
        return render(request, "main/shop.html", context)


class ShopDetailsView(LoginRequiredMixin, View):
    def get(self, request, slug):

        global avg_rating
        products = Product.objects.all()

        only_product = Product.objects.filter(slug=slug)

        reviews = Review.objects.filter(product=only_product[0]).order_by('-data_added')

        product_ratings = {}
        for product in products:
            avg_rating = Review.objects.filter(product=only_product[0].id).aggregate(Avg('rating'))['rating__avg']
            avg_rating = avg_rating if avg_rating is not None else 5
            product_ratings[f"{product.id}"] = avg_rating

        products = products.filter(subcategory=only_product[0].subcategory)

        context = {
            "product": only_product[0],
            "products": products,
            'reviews': reviews,
            "rev_count": reviews.count,
            "avg_rating": product_ratings[f'{only_product[0].id}'],
            'items_count': count_item_product(request),
        }
        return render(request, "main/detail.html", context)

    def post(self, request, slug):
        new_review = Review()
        new_review.user = request.user
        product = Product.objects.get(slug=slug)
        new_review.product = product
        new_review.text = request.POST.get('text')
        new_review.rating = request.POST.get('rating')
        new_review.save()

        return redirect('product-detail', slug)


class CartPageView(LoginRequiredMixin, View):
    def get(self, request):

        user = request.user
        order = Order.objects.get(user=user)
        order_items = OrderItems.objects.filter(order=order, complete=False)
        total = 0
        if order_items.exists():
            for item in order_items:
                total = total + item.total_item()

        context = {
            "orderItems": order_items,
            'items_count': count_item_product(request),
            "total": total
        }
        return render(request, "main/cart.html", context=context)


@csrf_exempt
def update_item(request):
    data = json.loads(request.body)
    product_id = data["productId"]
    action = data["action"]

    product = Product.objects.get(pk=product_id)
    user = request.user
    order, created = Order.objects.get_or_create(user=user)

    new_items, created = OrderItems.objects.get_or_create(order=order, product=product)

    if action == 'add':
        if product.max_count > new_items.quantity:
            new_items.quantity += 1

    elif action == 'remove':
        new_items.quantity -= 1

    new_items.save()

    if new_items.quantity <= 0 or action == 'clear':
        new_items.delete()

    return JsonResponse("Product add: ", safe=False)


class CheckOutView(View):
    def get(self, request):

        cities = City.objects.all()
        user = request.user.pk
        order = Order.objects.get(user=user)
        order_items = OrderItems.objects.filter(order=order)
        total = 0
        if order_items.exists():
            for item in order_items:
                total = total + item.total_item()

        context = {
            "orderItems": order_items,
            'items_count': count_item_product(request),
            "total": total,
            "cities": cities,
        }
        return render(request, 'main/checkout.html', context=context)

    def post(self, request):
        user = request.user
        tel_number = request.POST['t_number']
        address = request.POST['location']
        delicery_address = DeliveryAddress()
        delicery_address.order = Order.objects.get(user=user)
        delicery_address.city = City.objects.filter(name=address)[0]
        delicery_address.tel_number = tel_number
        delicery_address.save()

        order = Order.objects.get(user=user)
        items = OrderItems.objects.filter(order=order)
        for item in items:
            product = Product.objects.filter(pk=item.product.pk)[0]
            product.max_count -= item.quantity
            product.delete_product()
            item.delete()

        orderitems = OrderItems.objects.all(complete=False)
        for orderitem in orderitems:
            orderitem.check_count()
        return redirect("home")

