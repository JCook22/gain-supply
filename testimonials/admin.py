from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'rating',
        'headline',
    )

    ordering = ('rating',)


admin.site.register(Testimonial, TestimonialAdmin)