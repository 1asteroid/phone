from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, SubCategory
from customer.models import Order, OrderItems, Appeal
from customer.views import count_item_product


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

        if category_id:
            products = products.filter(subcategory=category_id)

        if name:
            products = products.filter(name__icontains=name)

        context = {
            "products": products,
            "subcategories": subcategories,
            "recent_products": products.order_by("-data_added"),
            'items_count': count_item_product(request)
        }
        return render(request, "main/index.html", context)


class ContactPageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "main/contact.html", {'items_count': count_item_product(request)})

    def post(self, request):
        form = request.POST
        message = form['message']
        if message:
            appeal = Appeal()
            appeal.user = request.user
            appeal.message = message
            appeal.save()
            print("saved")

            return render(request, 'main/contact.html', {'items_count': count_item_product(request), 'formReply': "So'rov qabul qilindi"})

        return render(request, 'main/contact.html', {'items_count': count_item_product(request)})


