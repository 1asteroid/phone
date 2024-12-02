# Generated by Django 5.0.3 on 2024-05-29 13:54

import django.db.models.deletion
import product.helpes
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='category', upload_to=product.helpes.SaveImagesCategory.product_images_path)),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='product_sub_id_07155b_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('category', models.CharField(choices=[('men', 'men'), ('women', 'women'), ('kids', 'kids'), ('all', 'all')], default='men', max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_type', models.CharField(choices=[('$', 'USD'), ('som', 'UZS')], default='$', max_length=5)),
                ('image', models.ImageField(upload_to=product.helpes.SaveImages.product_images_path)),
                ('max_count', models.PositiveIntegerField()),
                ('color', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('other', 'other'), ('mix', 'mix')], default='white', max_length=20)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('XXXXL', 'XXXXL'), ('dont', 'dont')], max_length=20)),
                ('description', models.TextField()),
                ('is_discount', models.BooleanField(default=False)),
                ('discount_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('view_count', models.PositiveBigIntegerField(default=0)),
                ('data_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='product_rev_id_80e37e_idx')],
            },
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id'], name='product_pro_id_06b227_idx'),
        ),
    ]