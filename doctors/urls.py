from django.urls import path
from .views import ListDoctorsView, DetailDoctorsView

from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
urlpatterns = [
    path('doctors',ListDoctorsView.as_view()),
] + router.urls
