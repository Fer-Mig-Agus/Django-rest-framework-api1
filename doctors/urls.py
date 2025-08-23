from django.urls import path
from .views import ListDoctorsView, DetailDoctorsView

urlpatterns = [
    path('doctors',ListDoctorsView.as_view()),
    path('doctors/<int:pk>/',DetailDoctorsView.as_view())
]
