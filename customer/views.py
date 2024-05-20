from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Avg

import json
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product, SubCategory, Review
from customer.models import Order, OrderItems


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
        }
        return render(request, "main/shop.html", context)


class ShopDetailsView(LoginRequiredMixin, View):
    def get(self, request, slug):

        global avg_rating
        products = Product.objects.all()

        only_product = products.filter(slug=slug)

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
        }
        return render(request, "main/detail.html", context)

    def post(self, request, slug):
        print(request)
        new_review = Review()
        new_review.user = request.user
        print("-------------", slug)
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
        order_items = OrderItems.objects.filter(order=order)
        context = {
            "orderItems": order_items
        }
        return render(request, "main/cart.html", context=context)
