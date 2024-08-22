from django.shortcuts import render
from .models import Testimonial

def all_testimonials(request):
    """
    Displays all testimonials in the database to the user
    """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)
    
