from django.contrib import admin
from .models import EmployeeProfile


class EmployeeProfileAdmin(admin.ModelAdmin):
    """
    Adds information on employess for admin users to view.
    """
    list_display = (
        'full_name',
        'role',
        'email',
        'telephone_number',
    )

    ordering = ('full_name',)


admin.site.register(EmployeeProfile, EmployeeProfileAdmin)
