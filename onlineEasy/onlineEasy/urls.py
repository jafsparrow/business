"""onlineEasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#local import
from product.views import create_product, update_product, all_products, view_product
from mainusers.views import admin_view, product_list, distributor_list, all_distributors,add_distributor, view_distributor, update_distributor
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #site admin user area.
    url(r'^administration/$', admin_view, name='admin_view'),
    url(r'^administration/products$', product_list, name='product_list'),
    url(r'^administration/distributors$', distributor_list, name='distributor_list'),

    # products related URLs
    url(r'^products$', all_products, name='all_products'),
    url(r'^product/(?P<id>\d+)$', view_product, name='view_product'),
    url(r'^product/add/$',create_product, name ='create_product' ),
    url(r'^product/(?P<id>\d+)/update$',update_product, name='update_product'),

    # distributer URLs.
    url(r'^distributors/$', all_distributors, name = 'all_distributors'),
    url(r'^distributor/add/$', add_distributor, name = 'add_distributor'),
    url(r'^distributors/(?P<id>\d+)/$', view_distributor, name='view_distributor'),
    url(r'^distributors/(?P<id>\d+)/update$', update_distributor, name='update_distributor'),

]
