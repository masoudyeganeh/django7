from django.urls import path
from views import *

urlpatterns = [
    path('/list', post_lists)
]