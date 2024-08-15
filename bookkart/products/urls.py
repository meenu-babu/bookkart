from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('list_products', views.product_list,name='product_list'),
    path('detail_products', views.product_details,name='product_details')
]
