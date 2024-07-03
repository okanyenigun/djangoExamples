from django.urls import path
from .views import ResultView, MainView


urlpatterns = [
    path('loading/',ResultView.ajax_view, name="pleasewait_loading"),
    path('', MainView.as_view(),name="pleasewait_main"),
    path('results/',ResultView.as_view(),name="pleasewait_result"),
    path('loading/',ResultView.ajax_view,name="pleasewait_loading"),
]