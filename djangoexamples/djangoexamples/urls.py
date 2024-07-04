from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajaxChartjs/', include('ajax_chartjs.urls')),          
    path('loginRegister/', include('login_regist.urls')),          
    path('pleasewait/', include('pleasewait.urls')),          
    path('autocomplete/', include('autocomplete.urls')),          
]
