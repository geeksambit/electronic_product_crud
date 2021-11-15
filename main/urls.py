"""main URL Configuration

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
from django.urls import path,include
from rest_framework.routers import DefaultRouter


from users import views as users_views
from products import views as products_views

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='user')
router.register(r'products', products_views.ProductViewSet, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', users_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/product/', products_views.ProductView.as_view(), name='products'),
    path('api/v1/product/<str:id>/', products_views.SecondProductViewSet.as_view(), name='product'),
    path('api/v1/product-attribute/', products_views.ProductAttributeView.as_view(), name='product_attributes'),
    path('api/v1/product-attribute/<str:id>/', products_views.ProductAttributeDetails.as_view(), name='product_attribute'),
    path('api/v1/mobiles', products_views.MobilesView.as_view(), name='mobiles'),
    path('api/v1/laptops', products_views.LaptopsView.as_view(), name='laptops'),
    
]