from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.urls import reverse_lazy
from profiles.models import UserProfile
from .models import Product, Category, Review
from .forms import ProductForm, CategoryForm, ReviewForm
from django.db.models import Avg

from wishlist.models import Wishlist, WishlistItem

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) \
                | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all().filter(name=product).order_by('-created_on')
    review_count = len(reviews)
    is_in_wishlist = False

    if request.user.is_authenticated:
        user = request.user
        wishlist_exists = Wishlist.objects.filter(
            user__user=user, product=product
        ).exists()
        is_in_wishlist = wishlist_exists

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews.create(
                user=user_profile,
                product=product,
                rating=request.POST.get('rating'),
                body=request.POST.get('body'))

            # Update the product's rating and review count
            reviews = Review.objects.filter(product=product)
            rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.rating = rating
            product.review_count = reviews.count()
            product.save()

            messages.success(request, 'Review successfully added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')

    else:
        form = ReviewForm()
        if request.user.is_authenticated:
            reviewed = Review.objects.all().filter(
                name=product).filter(user=user_profile.id)
        else:
            reviewed = False

    context = {
        'product': product,
        'form': form,
        'is_in_wishlist': is_in_wishlist,
        'reviews': reviews,
        'review_count': review_count,
        'reviewed': reviewed,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_category(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added category!')
            form = CategoryForm()  # Reset the form after saving the category
        else:
            messages.error(request, 'Failed to add a new category. \
                Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'products/add_category.html'
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    """ Edit a category on add category page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated category!')
            return redirect(reverse('add_category'))
        else:
            messages.error(
                request,
                'Failed to update category. Please ensure the form is valid.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.friendly_name}')

    template = 'products/edit_category.html'
    context = {
        'form': form,
        'category': category,
        'on_page': True,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ Delete a category"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted')

    return redirect(reverse('add_category'))


@login_required
def edit_review(request, review_id):
    """ Edit review"""
    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if request.user.id != review.user.user.id:
        messages.error(request, 'Sorry, you do not have access to that.')
        return redirect(
            reverse('product_detail', args=[product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            reviews = Review.objects.all().filter(product=product)
            rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.rating = rating
            product.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update review - please check form and try again")
    else:
        form = ReviewForm(instance=review)

    messages.info(request, f"You are editing your review of {product}.")
    template = 'products/product_detail.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete review """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if request.user.id != review.user.user.id:
        messages.error(request, 'Sorry, you do not have access to that.')
        return redirect(
            reverse('product_detail', args=[product.id]))

    review.delete()
    reviews = Review.objects.all().filter(product=product)
    rating = reviews.aggregate(Avg('rating'))['rating__avg']
    product.rating = rating
    product.review_count -= 1
    product.save()
    messages.success(request, 'Review successfully deleted!')
    return redirect(reverse('product_detail', args=[product.id]))