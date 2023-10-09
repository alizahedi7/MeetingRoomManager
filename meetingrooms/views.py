from django.shortcuts import render, redirect
from .forms import MeetingRoomReservationForm


def reserve_meeting_room(request):
    if request.method == "POST":
        form = MeetingRoomReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.status = "pending"
            reservation.save()

            return redirect("reservation_success")
    else:
        form = MeetingRoomReservationForm()

    return render(request, "meetingroom/reservation_form.html", {"form": form})

def reservation_success(request):
    return render(request, 'meetingroom/reservation_success.html')
