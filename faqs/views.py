from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Faqs


def faqs(request):
    """
    Display faqs in the faqs page
    """
    faqs = Faqs.objects.all()

    template = 'faqs/faqs.html'

    context = {
        'faqs': faqs,
    }

    return render(request, template, context)
