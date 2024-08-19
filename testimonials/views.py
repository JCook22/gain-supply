from django.shortcuts import render
from .models import Testimonial

def all_testimonials(request):
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html')
    
