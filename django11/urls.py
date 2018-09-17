from django.contrib import admin
from django.conf.urls import url, include

from apps.home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index),
    url('home/', include('apps.home.urls')),
    url('account/', include('apps.account.urls')),
    url('cate/', include('apps.cate_detail.urls')),
    url('order/', include('apps.order.urls')),
    url('cart/', include('apps.cart.urls')),
    url('pay/', include('apps.pay.urls')),
    url('shop/', include('apps.shop_detail.urls')),
]
