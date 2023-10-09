# meetingrooms/admin.py
from django.contrib import admin

from .models import MeetingRoom, MeetingRoomReservation


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity")
    search_fields = ("name",)
    list_filter = ("capacity",)


@admin.register(MeetingRoomReservation)
class MeetingRoomReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "meeting_room", "requested_datetime", "status")
    list_filter = ("status", "meeting_room__name", "requested_datetime")
    search_fields = ("user__user__username", "meeting_room__name")

    def meeting_room(self, obj):
        return obj.meeting_room.name

    meeting_room.short_description = "Meeting Room"
