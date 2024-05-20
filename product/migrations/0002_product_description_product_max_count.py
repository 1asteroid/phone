# Generated by Django 5.0.3 on 2024-05-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='max_count',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
