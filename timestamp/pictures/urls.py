from django.urls import path
from pictures import views

urlpatterns = [
    path('pictures/', views.PictureList),
]