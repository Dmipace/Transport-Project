from django.urls import re_path
from TransportOrderApp import views


urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^customer$',views.customerApi),
    re_path(r'^customer/([0-9]+)$',views.customerApi),
    re_path(r'^customer/([0-9]+)/edit$',views.customerApi)
]
















