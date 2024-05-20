import uuid
from django.db.models import TextChoices


class SaveImages(object):
    def product_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"product/{uuid.uuid4()}.{image_extension}"


class SaveImagesCategory(object):
    def product_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"category/{uuid.uuid4()}.{image_extension}"


class CategoryChoise(TextChoices):
    men = "men", "men"
    women = "women", "women"
    kids = "kids", "kids"
    all = "all", "all"


class ColorChoise(TextChoices):
    black = "black", "black"
    white = "white", "white"
    red = "red", "red"
    blue = "blue", "blue"
    green = "green", "green"
    other = "other", "other"
    mix = "mix", "mix"


class SizesProduct(TextChoices):
    xs = "XS", "XS"
    s = "S", "S"
    m = "M", "M"
    l = "L", "L"
    xl = "XL", "XL"
    xxl = "XXL", "XXL"
    xxxl = "XXXL", "XXXL"
    xxxxl = "XXXXL", "XXXXL"
    no_need = "dont", "dont"   # bazi maxsulotlar uchun razmer shart emas


class PriceType(TextChoices):
    dollar = '$', 'USD'
    som = "som", "UZS"
