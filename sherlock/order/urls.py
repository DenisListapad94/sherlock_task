from django.urls import path, include
from .views import display_manufacturer

urlpatterns = [
    path("manufacturer/<int:contract_id>", display_manufacturer)
]
