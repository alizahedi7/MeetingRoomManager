from django.db import models


class MeetingRoom(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class MeetingRoomReservation(models.Model):
    user = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    requested_datetime = models.DateTimeField()
    number_of_people = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=(
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ),
        default="pending",
    )

    def __str__(self):
        return f"Reservation by {self.user} for {self.meeting_room} at {self.requested_datetime}"
