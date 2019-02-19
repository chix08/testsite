from django.contrib import admin
from django.urls import path

from .views import post_model_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_model_list, name='post_model_list')
]
