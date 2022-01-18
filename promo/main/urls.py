from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.index,name="Index"),
    path('action',views.action,name="Action"),
    path('company',views.company,name="Company")
]
