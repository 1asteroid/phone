import uuid
from django.db.models import TextChoices


class SaveImages(object):
    def customer_images_path(instance, filename):
        image_extension = filename.split('.')[:-1]
        return f"customer_image/{uuid.uuid4()}.{image_extension}"