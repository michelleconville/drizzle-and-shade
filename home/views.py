from django.shortcuts import render


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')


def privacy(request):
    """A view to return the privacy policy page"""
    return render(request, "home/privacy_policy.html")


def terms(request):
    """A view to return the terms and conditions page"""
    return render(request, "home/terms.html")
