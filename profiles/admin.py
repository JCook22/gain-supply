from django.contrib import admin
from .models import EmployeeProfile


class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'role',
        'email',
        'telephone_number',
    )

    ordering = ('full_name',)


admin.site.register(EmployeeProfile, EmployeeProfileAdmin)
