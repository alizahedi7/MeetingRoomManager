from django.urls import path

from . import views

urlpatterns = [
    path(
        "reserve-meeting-room/", views.reserve_meeting_room, name="reserve_meeting_room"
    ),
    path("reservation-success/", views.reservation_success, name="reservation_success"),
]
