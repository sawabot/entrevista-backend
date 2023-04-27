from django.urls import path

from oms.api import api

urlpatterns = [
    path('', api.urls),
]
