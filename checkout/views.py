from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import Orderform


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You haven't added any prodcts yet.")
        return redirect(reverse('products'))

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)