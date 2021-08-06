from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JLQWwKWb2nRH4X27HapSZNDGHpoW4ezBgbDleKmNRxxFhAeydrzZT2LMFcPbqVWxdtr2YvxmV1YLt3USibpk2Zo00FfrJRe5u',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
