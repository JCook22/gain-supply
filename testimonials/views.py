from django.shortcuts import render
from .models import Testimonial

def all_testimonials(request):
    testimonials = Testimonial.
