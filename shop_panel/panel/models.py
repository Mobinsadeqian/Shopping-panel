from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام دسته بندی')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name 
    

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="دسته‌بندی محصول"
    )

    name = models.CharField(blank=True, max_length=100, verbose_name="نام محصول")
    price = models.BigIntegerField(blank=True, null=True, verbose_name="قیمت")
    model = models.CharField(blank=True, max_length=100, verbose_name="مدل")
    detail = models.TextField(blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name


   
