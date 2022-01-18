from django.urls import path

from api.views import fruit_detail, fruit_list, region_list, region_detail


urlpatterns = [
    path('region/', region_list),
    path('region/<int:pk>/', region_detail),
    path('fruit/', fruit_list),
    path('fruit/<int:pk>/', fruit_detail),
]
