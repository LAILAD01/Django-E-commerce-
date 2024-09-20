"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from mysite import views

urlpatterns = [
    path("mysite/", include("mysite.urls")),
    path('admin/', admin.site.urls),
    path('home/', views.home , name='home'),
    path('shop/', views.shop, name='shop'),
    path('blog/', views.blog , name='blog'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('cart/', views.cart , name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.user_login , name='login'),
    path('signup/', views.signup , name='signup'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)