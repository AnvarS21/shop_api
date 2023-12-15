"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import SimpleRouter
from category.views import CategoryViewSet
from order.views import OrderAPIView
from product.views import ProductViewSet
from .drf_swagger import urlpatterns as doc_urls

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/orders/', OrderAPIView.as_view()),
]

urlpatterns += doc_urls # swagger docs urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
