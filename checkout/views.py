from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, "There's nothing in your shopping bag at the moment"
            )
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NP7V1IAQ5RnOlLE0L6ESJsvhecBet0o0N0YllTENmTrDoQKHBlp96gdtWPolOF3CXSsYI5PteMGadsDj6vxwL9200HR6Vhwe5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
