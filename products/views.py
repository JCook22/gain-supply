from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request): 
    """
    Shows the user all products and allows them to sort or filter them
    """
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
                messages.error(request, "The search bar cannot be empty.")
                return redirect(reverse('products'))

            queries  = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products' : products,
        'search_term' : query,
        'current_categories': categories,
        'current_sorting' : current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id): 
    """
    Shows the user the details of a selected product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ 
    Allows admin users to add new products to site
    """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added to database successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Attempt to add product has failed! Please check the form data for errors.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ 
    Allows admin users to edit products on the site
    """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have succesfully updated the product.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Attempt to edit product has failed! Please check the form data for errors.')
    else:   
        form = ProductForm(instance=product)
        messages.info(request, f'You have chosen to edit {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ 
    Allows admin users to delete products on the site
    """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect(reverse('products'))