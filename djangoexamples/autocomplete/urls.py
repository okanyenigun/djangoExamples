from django.urls import path
from autocomplete.views import get_homeview,search_person

urlpatterns = [
    path('', get_homeview, name="autocomplete_home"),
    path('search/', search_person),

]