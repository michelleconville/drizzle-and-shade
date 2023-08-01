from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.urls import reverse_lazy
from profiles.models import UserProfile
from .models import Product, Category, Review
from .forms import ProductForm, CategoryForm, ReviewForm, UpdateStockForm
from django.db.models import Avg
from django.db import models
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    paginator = Paginator(products, 8)
    page = request.GET.get('page')

    try:
        paginated_products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results.
        paginated_products = paginator.page(paginator.num_pages)

    for product in paginated_products:
        product.stock_message = product.low_stock_message()

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': paginated_products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


@login_required
def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all().filter(product=product).order_by('-created_on')
    review_count = len(reviews)
    is_in_wishlist = False

    if request.user.is_authenticated:
        user = request.user
        wishlist_exists = Wishlist.objects.filter(
            user__user=user, product=product
        ).exists()
        is_in_wishlist = wishlist_exists

        user_profile = get_object_or_404(UserProfile, user=request.user)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.product = product
                review.name = product.name
                review.save()

                # Update the product's rating and review count
                reviews = Review.objects.filter(product=product)
                rating = reviews.aggregate(Avg('rating'))['rating__avg']
                product.rating = rating
                product.review_count = reviews.count()
                product.save()

                messages.success(request, 'Review successfully added')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add review. \
                    Please ensure the form is valid.')

        else:
            form = ReviewForm()

    else:
        form = ReviewForm()

    # Get the current stock quantity of the product
    stock_quantity = product.quantity

    if request.method == 'POST':
        # Get the quantity requested by the user from the form
        quantity_requested = int(request.POST.get('quantity', 1))

        # Check if the requested quantity is greater than the available stock
        if quantity_requested > stock_quantity:
            messages.error(request, 'Sorry, there is not enough stock available for this quantity.')
            # You can redirect the user back to the product detail page or handle the error as needed.
        else:
            # Quantity requested is valid, add the product to the bag
            # Implement the code to add the product to the bag here
            pass  # Replace 'pass' with your code for adding the product to the bag

    context = {
        'product': product,
        'form': form,
        'is_in_wishlist': is_in_wishlist,
        'reviews': reviews,
        'review_count': review_count,
        'is_out_of_stock': product.is_out_of_stock,
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

    if request.user.id != review.user.id:
        messages.error(request, 'Sorry, you do not have access to that.')
        return redirect(reverse('product_detail', args=[product.id]))

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

    if request.user.id != review.user.id:
        messages.error(request, 'Sorry, you do not have access to that.')
        return redirect(reverse('product_detail', args=[product.id]))

    review.delete()
    reviews = Review.objects.all().filter(product=product)
    rating = reviews.aggregate(Avg('rating'))['rating__avg']
    product.rating = rating
    product.review_count -= 1
    product.save()
    messages.success(request, 'Review successfully deleted!')
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def stock_levels(request):
    """
    View current stock levels
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can do that.')
        return redirect(reverse('home'))

    stock_levels = Product.objects.all().order_by('-name')
    template = 'products/stock_levels.html'
    context = {
        'stock_levels': stock_levels,
    }
    return render(request, template, context)


@login_required
def update_stock(request, product_id):
    """
    View to update stock levels for store owners
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can do that.')
        return redirect(reverse('home'))

    stock_level = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = UpdateStockForm(request.POST, instance=stock_level)
        if form.is_valid():
            form.save()
            return redirect('stock_levels')
    else:
        form = UpdateStockForm(instance=stock_level)
    template = 'products/update_stock.html'
    context = {
        'form': form,
        'product': stock_level,
        }
    return render(request, template, context)
