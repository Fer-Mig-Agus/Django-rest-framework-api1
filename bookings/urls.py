from django.urls import path
from .views import ListAppointmentsView, DetailsAppointmentsView, ListMedicalNotesView, DetailMedicalViewsView

urlpatterns = [
    path('bookings/appointments',ListAppointmentsView.as_view()),
    path('bookings/appointments/<int:pk>/',DetailsAppointmentsView.as_view()),
    path('bookings/medicals',ListMedicalNotesView.as_view()),
    path('bookings/medicals/<int:pk>/',DetailMedicalViewsView.as_view())
]
