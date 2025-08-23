from django.urls import path
from .views import DetailPatientsView, ListPatientsView

urlpatterns = [
    path('patients', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientsView.as_view()),
]
