from django import forms

from .models import MeetingRoomReservation


class MeetingRoomReservationForm(forms.ModelForm):
    class Meta:
        model = MeetingRoomReservation
        fields = ["meeting_room", "requested_datetime", "number_of_people"]
