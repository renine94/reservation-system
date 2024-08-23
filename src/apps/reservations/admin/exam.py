from django.contrib import admin

from src.apps.reservations.models.exam import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass
    # list_display = ["username", "email", "is_superuser", "is_staff", "is_active", "created_at"]
    # list_filter = ["is_staff", "is_active"]
    # search_fields = ["username", "email"]
