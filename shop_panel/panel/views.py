from django.shortcuts import render, get_object_or_404
from .models import Product, Category # اضافه شدن Category

def main_page(request):
    """
    نمایش صفحه اصلی
    """
    return render(request, 'panel/main_page.html')

def product_detail(request, id):
    """
    نمایش جزئیات یک محصول خاص
    """
    product = get_object_or_404(Product, id=id)
    return render(request, 'panel/product_detail.html', {'product': product})

def product_list(request):
    """
    نمایش لیست محصولات با امکان فیلتر بر اساس دسته‌بندی و جستجو
    """
    # دریافت پارامترهای جستجو و فیلتر
    category_id = request.GET.get('cat')
    query = request.GET.get('q')

    # شروع با تمام محصولات
    products = Product.objects.all()

    # فیلتر بر اساس دسته‌بندی
    if category_id:
        # مطمئن می‌شویم که category_id عدد است
        try:
            category_id = int(category_id)
            products = products.filter(category__id=category_id)
        except ValueError:
            # اگر category_id نامعتبر بود، لیست محصولات همان all باقی می‌ماند
            pass

    # فیلتر بر اساس جستجو (نام یا مدل)
    if query:
        # فیلتر کردن محصولاتی که نام یا مدل آن‌ها شامل عبارت جستجو باشد (case-insensitive)
        from django.db.models import Q
        products = products.filter(Q(name__icontains=query) | Q(model__icontains=query))
    
    # دریافت تمام دسته‌بندی‌ها برای نمایش در سایدبار
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category_id': category_id,
        # request.GET.q در تمپلیت قابل دسترسی است و نیازی به ارسال مجدد نیست
    }

    return render(request, 'panel/product_list.html', context)