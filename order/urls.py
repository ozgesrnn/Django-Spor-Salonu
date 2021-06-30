from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('addtocart/<int:id>' , views.addtocart, name="addtocart"),
    path('orderproduct/' , views.orderproduct, name="orderproduct"),

]