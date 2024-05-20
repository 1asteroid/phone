from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, SubCategory


class BaseView(View):
    def get(self, request):
        products = Product.objects.all()
        subcategories = SubCategory.objects.all()

        context = {
            "products": products,
            "subcategories": subcategories,
        }
        return render(request, "main/base.html", context)


class HomePageView(View):
    def get(self, request):
        products = Product.objects.all()
        subcategories = SubCategory.objects.all()

        name = request.GET.get('name')
        category_id = request.GET.get('category_id')
        print(category_id)
        if category_id:
            products = products.filter(subcategory=category_id)

        if name:
            products = products.filter(name__icontains=name)

        context = {
            "products": products,
            "subcategories": subcategories,
            "recent_products": products.order_by("-data_added"),
        }
        return render(request, "main/index.html", context)


