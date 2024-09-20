from . import views
from django.urls import path


#from mysite import *


app_name = 'mysite'

urlpatterns = [
    path('home/', views.home , name='home'),
    path('shop/', views.shop , name='shop'),
    path('blog/', views.blog , name='blog'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('cart/', views.cart , name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.user_login , name='login'),
    path('signup/', views.signup , name='signup'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]