from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm, UserForm

from checkout.models import Order


@login_required()
def profile(request):
    """
    Display the User's profile
    """
    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        userform = UserForm(request.POST, instance=user)
        profileform = UserProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, "Profile updated successfully")
            return redirect(("profile"))

    userform = UserForm(instance=user)
    profileform = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "profile": profile,
        "userform": userform,
        "profileform": profileform,
        "orders": orders,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
def delete_profile(request, username):
    """
    Query the database for the User that matches the profile user
    and deletes user & profile
    """
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)

    if user != profile.user:
        messages.success(request, "You are not authorized \
             to delete this Profile.")
        return redirect("profile")

    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, "Sorry to see you go, \
            your Account has been deleted.")
        return redirect("home")

    context = {"username": username}
    return render(request, "profiles/profile.html", context)


def order_history(request, order_number):
    """
    Display order history
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def product_management(request):
    """
    Display product management page where admin
    can choose to add category and umbrella
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))
    template = 'profiles/product_management.html'
    return render(request, template)


@login_required
def admin_panel(request):
    """
    Display admin account overview
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    template = 'profiles/admin_panel.html'
    return render(request, template)


@login_required
def account_overview(request):
    """
    Display the account overview
    """
    template = 'profiles/account_overview.html'
    return render(request, template)
