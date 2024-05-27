# Generated by Django 5.0.4 on 2024-05-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_initial'),
        ('customer', '0004_alter_order_options_alter_orderitems_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='deliveryaddress',
            options={'ordering': ['id']},
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['id'], name='address_cit_id_93cf67_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['id'], name='address_cou_id_e14fb5_idx'),
        ),
        migrations.AddIndex(
            model_name='deliveryaddress',
            index=models.Index(fields=['id'], name='address_del_id_97f7ce_idx'),
        ),
    ]