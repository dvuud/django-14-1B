from django.urls import path
from apps.secondary.views import index

urlpatterns = [
    path('', index, name='index_url')
]