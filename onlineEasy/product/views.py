from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


from product.forms import ProductCreateForm, ProductUpdateForm
from mainusers.models import Producer
from product.models import Product
# Create your views here.

def all_products(request):
    products = Product.products.all()
    context = {'products': products}
    return render(request, 'product/product_list.html', context)

def view_product(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


def create_product(request):

    if request.method == 'POST':
        form=ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.active = True
            product.producer = Producer.objects.first()
            product.save()
            #context = {'form': form }
        return HttpResponseRedirect(reverse(view_product,  kwargs={'id':product.id  }))#render(request, 'product/create_product.html', context)
    else:
        form = ProductCreateForm()
        context = {'form': form }
        return render(request, 'product/create_product.html', context)


def update_product(request, id):
    product=get_object_or_404(Product, id=id)
    if request.method =='POST':
        form=ProductUpdateForm(request.POST, instance=product)
        context = {'form': form,
                    'product':product }
        if form.is_valid():
            product = form.save(commit=False)
            product.producer = Producer.objects.first()
            form.save()
            return HttpResponseRedirect(reverse(all_products))
    else:
        form=ProductUpdateForm(instance=product)
        context = {'form': form,
                    'product':product }
        return render(request, 'product/update_product.html',context)
