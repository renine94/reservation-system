from django.contrib import admin

from src.apps.reservations.models.reservation import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
    # list_display = ["username", "email", "is_superuser", "is_staff", "is_active", "created_at"]
    # list_filter = ["is_staff", "is_active"]
    # search_fields = ["username", "email"]
