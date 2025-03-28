from django.db import models

# Create your models here.
class Zero_Product(models.Model):
    id = models.AutoField(primary_key=True)
    Manufacturer = models.CharField(default="Unknown", max_length=50, verbose_name="제조사명")
    product_name = models.CharField(max_length=50, verbose_name="제품명")
    Capacity =  models.CharField(max_length=50, default=0, verbose_name="용량 (g)")
    Product_calorific_value = models.CharField(max_length=50, default=0, verbose_name="열량 (g)")
    carbohydrates = models.CharField(max_length=50, verbose_name="탄수화물 (g)")
    protein =models.CharField(max_length=50, verbose_name="단백질 (g)")
    fat = models.CharField(max_length=50, verbose_name="지방 (g)")
    saturated_fat = models.CharField(max_length=50, default=0, verbose_name="포화지방 (g)")
    trans_fat = models.CharField(max_length=50, default=0, verbose_name="트렌스지방 (g)")
    Cholesterol = models.CharField(max_length=50, default=0, verbose_name="콜레스테롤 (mg)")
    sodium = models.CharField(max_length=50, default=0, verbose_name="나트륨 (mg)")
    Caffeine = models.CharField(max_length=50, default=0,verbose_name="카페인 (g)")
    sugar = models.CharField(max_length=50, default=0, verbose_name="당류 (g)")
    Sugar_alcohol =  models.CharField(max_length=50, default=0, verbose_name="당알콜 (g)")
    maltitol = models.CharField(max_length=50, default=0, verbose_name="말티톨 (g)")
    maltitol_syrup = models.CharField(max_length=50, default=0, verbose_name="말티톨 시럽 (g)")
    glucose_syrup = models.CharField(max_length=50, default=0, verbose_name="물엿 (g)")
    GI = models.CharField(max_length=50, default=0, verbose_name="GI지수")
    GL = models.CharField(max_length=50, default=0, verbose_name="GL지수")
    Raw_materials = models.TextField(default="Unknown", max_length=255, verbose_name="원재료명")
    emoji = models.CharField(max_length=20, default="😊")
    def __str__(self):
        return self.product_name
        # product_name이 물건의 이름이고, __str__은 그 이름을 말해준다.
    class Meta:
        verbose_name = "제로식품"
        verbose_name_plural = "제로식품 목록"
        # Django 관리자 페이지에서 모델이 "제로식품 목록"으로 보이고
        # 각 객체는 product_name으로 구별됩니다.