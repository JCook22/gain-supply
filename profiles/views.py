from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is order confirmation for order number {order_number}.'
        'The confirmation email was sent on the date of the order.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)
    