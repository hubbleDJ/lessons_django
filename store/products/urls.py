from django.urls import path
from products.views import products, basket_add, basket_remove

app_name = 'products'
urlpatterns = [
    path('', products, name='index'), #страница  с товарами
    path('category/<int:category_id>/', products, name='category'), #страница  с товарами
    path('page/<int:page_num>/', products, name='paginator'), #страница  с товарами
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'), #добавление в корзину
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'), #добавление в корзину
]