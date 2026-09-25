from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # مسارات الحسابات وتغيير اسم المستخدم
    path('logout/', shop_views.logout_view, name='logout'),
    path('register/', shop_views.register_view, name='register'),
    path('login/', shop_views.login_view, name='login'),
    path('change-username/', shop_views.change_username, name='change_username'),
    # مسارات المتجر الأساسية
    path('', shop_views.product_list, name='product_list'),
    path(
        'product/<int:pk>/', shop_views.product_detail, name='product_detail'
    ),  # <--- مسار تفاصيل المنتج
    path('ai-assistant/', shop_views.ai_assistant, name='ai_assistant'),
    path(
        'add-to-cart/<int:product_id>/',
        shop_views.add_to_cart,
        name='add_to_cart',
    ),
    path(
        'increase-cart/<int:item_id>/',
        shop_views.increase_cart_item,
        name='increase_cart_item',
    ),
    path(
        'decrease-cart/<int:item_id>/',
        shop_views.decrease_cart_item,
        name='decrease_cart_item',
    ),
    path(
        'remove-from-cart/<int:item_id>/',
        shop_views.remove_from_cart,
        name='remove_from_cart',
    ),
    path('clear-cart/', shop_views.clear_cart, name='clear_cart'),
    path('cart/', shop_views.cart_detail, name='cart_detail'),
    path('checkout/', shop_views.checkout, name='checkout'),
    # مسار صفحة نجاح الطلب الجديدة
    path('order-success/', shop_views.order_success, name='order_success'),
    # مسار سجل الطلبات (Order History)
    path('orders/', shop_views.order_history, name='order_history'),
    # مسارات الكورسات
    path('courses/', blog_views.index, name='index'),
    path(
        'coursesfromstaticlist/',
        blog_views.courses_static_view,
        name='courses_static_view',
    ),
    path('coursesfromdb/', blog_views.coursesfromdb, name='coursesfromdb'),
    path('add/', blog_views.add_course, name='add_course'),
    path('edit/<int:pk>/', blog_views.edit_course, name='edit_course'),
    path('delete/<int:pk>/', blog_views.delete_course, name='delete_course'),
    path('clear-ai-chat/', shop_views.clear_ai_chat, name='clear_ai_chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)