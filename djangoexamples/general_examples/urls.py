from django.urls import path
from general_examples.views import set_cookie, set_test_cookie, check_test_cookie, home

urlpatterns = [
    path('cookieSet/', set_cookie),
    path('setTestCookie/', set_test_cookie),
    path('checkTestCookie/', check_test_cookie),
    path("home/", home),
]