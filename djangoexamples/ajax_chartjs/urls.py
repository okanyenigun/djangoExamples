from django.urls import path
from .views import AjaxViewer


urlpatterns = [
    path('', AjaxViewer.as_view(),name="ajax_chartjs_index"),
]