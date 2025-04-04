# Generated by Django 4.2 on 2025-03-28 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zero_Product', '0002_zero_product_caffeine_zero_product_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zero_product',
            name='Caffeine',
            field=models.TextField(default=0, verbose_name='카페인 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='Cholesterol',
            field=models.TextField(default=0, verbose_name='콜레스테롤 (mg)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='GI',
            field=models.TextField(default=0, verbose_name='GI지수'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='GL',
            field=models.TextField(default=0, verbose_name='GL지수'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='Product_calorific_value',
            field=models.TextField(default=0, verbose_name='열량 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='Raw_materials',
            field=models.TextField(default='Unknown', max_length=255, verbose_name='원재료명'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='Sugar_alcohol',
            field=models.TextField(default=0, verbose_name='당알콜 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='carbohydrates',
            field=models.TextField(verbose_name='탄수화물 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='fat',
            field=models.TextField(verbose_name='지방 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='glucose_syrup',
            field=models.TextField(default=0, verbose_name='물엿 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='maltitol',
            field=models.TextField(default=0, verbose_name='말티톨 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='maltitol_syrup',
            field=models.TextField(default=0, verbose_name='말티톨 시럽 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='protein',
            field=models.TextField(verbose_name='단백질 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='saturated_fat',
            field=models.TextField(default=0, verbose_name='포화지방 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='sodium',
            field=models.TextField(default=0, verbose_name='나트륨 (mg)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='sugar',
            field=models.TextField(default=0, verbose_name='당류 (g)'),
        ),
        migrations.AlterField(
            model_name='zero_product',
            name='trans_fat',
            field=models.TextField(default=0, verbose_name='트렌스지방 (g)'),
        ),
    ]
