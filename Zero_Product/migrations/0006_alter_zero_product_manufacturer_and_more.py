# Generated by Django 4.2 on 2025-03-28 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zero_Product', '0005_alter_zero_product_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zero_product',
            name='Manufacturer',
            field=models.TextField(default='Unknown', max_length=50, verbose_name='제조사명'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='product_name',
            field=models.TextField(max_length=50, verbose_name='제품명'),
        ),
    ]
