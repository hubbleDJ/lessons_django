from django.urls import path
from products.views import basket_add, basket_remove, ProductsListView

app_name = 'products'
urlpatterns = [
    path('', ProductsListView.as_view(), name='index'), #страница  с товарами
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'), #страница  с товарами
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'), #страница  с товарами
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'), #добавление в корзину
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'), #добавление в корзину
]