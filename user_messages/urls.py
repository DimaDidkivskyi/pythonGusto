from django.urls import path
from .views import *

urlpatterns = [
    path('', messages_view),
]
