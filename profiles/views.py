from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Allows users to visit their profile page if they register
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully')
        else:
            messages.error(request,
                           'Attempt to update profile has failed!'
                           'Please check the form data for errors.')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Displays to the user a list of their previous orders if they have any
    """
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
