from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Faqs
from .forms import FaqsForm


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


@login_required
def add_faqs(request):
    """
    Add a new faqs to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! You are not authorised to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQs added successfully.')
            return redirect('faqs')
        else:
            messages.info(
                request, 'Failed to update FAQ.\
                     Please ensure the form is valid.'
            )
    else:
        form = FaqsForm()

    template = 'faqs/add_faqs.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faqs(request, item_id):
    """
    Edit a faqs and update to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! You are not authorised to do that')
        return redirect(reverse('home'))

    item = get_object_or_404(Faqs, pk=item_id)

    if request.method == 'POST':
        form = FaqsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQs updated successfully.')
            return redirect('faqs')
        else:
            messages.info(request, 'Failed to update product.\
                Please ensure the form is valid.')
    else:
        form = FaqsForm(instance=item)

    template = 'faqs/edit_faqs.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_faqs(request, item_id):
    """
    Delete a faqs from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! You are not authorised to do that')
        return redirect(reverse('home'))
    item = get_object_or_404(Faqs, pk=item_id)
    item.delete()
    messages.success(request, f'{item} is deleted successfully')
    return redirect('faqs')
