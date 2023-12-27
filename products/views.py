from django.shortcuts import render, HttpResponse, redirect
from products.forms import FormEditAdd
from products.models import Product

# Create your views here.


def home (request):
    
    products = Product.objects.all()

    return render(
        request,
        'home.html',
        {
            'products': products
        }
    )

def add (request):
    
    if request.method == 'POST':

        data = FormEditAdd(request.POST, request.FILES)

        if data.is_valid():
            product = data.cleaned_data

            name = product.get('name')
            price = product.get('price')
            available = product.get('available')
            description = product.get('text')
            img = request.FILES.get('img')

            product = Product (
                name=name,
                price=price,
                available = available,
                text=description,
                img = img
            )

            product.save()

            return redirect('home')

    
    form = FormEditAdd()
    return render(
        request,
        'form.html',
        {
            'title': 'Add Product 👌',
            'form': form
        }
    )

def delete (request, id):   
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('home')

def update (request, id):   
    
    if request.method == 'POST':
        data = FormEditAdd(request.POST).edit()
        if data.is_valid():
            
            product_form = data.cleaned_data
            name = product_form.get('name')
            price = product_form.get('price')
            available = product_form.get('available')
            description = product_form.get('text')

            product = Product.objects.get(pk=id)

            product.name=name
            product.price=price
            product.available = available
            product.text=description

            product.save()

            return redirect('home')    

    #GET 
    product = Product.objects.get(pk=id)    
    form = FormEditAdd().edit() 
    form.set_values(
        name=product.name,
        price=product.price,
        available=product.available,
        text=product.text
    )
    return render(
        request,
        'form.html',
        {
            'title': 'Update Product 👏',
            'form': form
        }
    )

def product(request,id):
    product = Product.objects.get(pk=id)
    return render(
        request,
        'product.html',
        {
            'product': product
        }
    )