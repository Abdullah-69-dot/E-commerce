from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Product, Category
import re

def product_list(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        products = products.filter(category=category)
        
    return render(request, 'products/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'products/product/detail.html', {'product': product})

def chatbot_view(request):
    user_message = request.GET.get("message", "").strip().lower()
    response = handle_user_message(user_message)
    return JsonResponse(response)

def handle_user_message(message):
    cleaned_msg = re.sub(r'[^\w\s\u0600-\u06FF]', '', message)
    
    # نمط البحث عن السعر
    price_pattern = r'(سعر|كام|ثمن|تكلفة|قيمة)\s+(.*)'
    if re.search(price_pattern, cleaned_msg):
        return handle_price_query(cleaned_msg)
    
    # نمط البحث عن المنتجات
    if re.search(r'(المنتجات|عرض|قائمة|ايه|محتويات)', cleaned_msg):
        return handle_products_query()
    
    # نمط البحث عن التصنيفات
    if re.search(r'(التصنيفات|اقسام|انواع|تصنيف)', cleaned_msg):
        return handle_categories_query()
    
    # الرد الافتراضي
    return {
        "reply": "عذرًا لم أفهم سؤالك. يمكنك طرح أسئلة مثل:<br>"
                "- ما هو سعر المنتج X؟<br>"
                "- ما هي المنتجات المتاحة؟<br>"
                "- ما هي التصنيفات الموجودة؟"
    }

def handle_price_query(message):
    match = re.search(r'(سعر|كام|ثمن|تكلفة|قيمة)\s+(.*)', message)
    product_name = match.group(2).strip()
    
    products = Product.objects.filter(
        Q(name__icontains=product_name) |
        Q(description__icontains=product_name),
        available=True
    ).distinct()[:3]
    
    if not products:
        return {"reply": f"لم يتم العثور على '{product_name}'. اكتب اسم المنتج بشكل أدق."}
    
    if len(products) > 1:
        product_list = "<br>".join([f"{p.name} - {p.price} جنيه" for p in products])
        return {"reply": f"وجدت عدة منتجات:<br>{product_list}<br>الرجاء تحديد اسم أدق."}
    
    return {"reply": f"سعر {products[0].name} هو {products[0].price} جنيه 💵"}

def handle_products_query():
    products = Product.objects.filter(available=True).order_by('-created')[:5]
    if products:
        product_list = "<br>- ".join([p.name for p in products])
        return {"reply": f"أحدث المنتجات:<br>- {product_list}"}
    return {"reply": "لا توجد منتجات متاحة حالياً."}

def handle_categories_query():
    categories = Category.objects.all()[:5]
    if categories:
        category_list = "<br>- ".join([c.name for c in categories])
        return {"reply": f"التصنيفات الرئيسية:<br>- {category_list}"}
    return {"reply": "لا توجد تصنيفات متاحة حالياً."}