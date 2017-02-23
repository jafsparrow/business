from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect

#local apps
from product.models import Product
from mainusers.models import Distributor
from mainusers.forms import DistributorCreateForm, DistributorUpdateForm
# Create your views here.
def admin_view(request):
    products = Product.products.count()
    distributors = Distributor.objects.count()
    context = {'products': products,
                'distributors':distributors,
                }
    return render(request, 'mainusers/admin.html', context)


def product_list(request):
    products = Product.products.all()
    context = {'products': products}
    return render(request, 'mainusers/productslist.html', context)


def distributor_list(request):
    pass

def all_distributors(request):
    distributors = Distributor.objects.all()
    context ={'distributors': distributors }
    return render(request, 'mainusers/distributor_list.html', context)

def add_distributor(request):
    if request.method  == 'POST':
        form =DistributorCreateForm(request.POST)
        if form.is_valid():
            distributer = form.save()
            return HttpResponseRedirect(reverse(view_distributor,  kwargs={'id':distributer.id  }))
    else:
        form =DistributorCreateForm()
        context ={'form': form }
        return render(request, 'mainusers/distributor/create_distributor.html', context)



def view_distributor(request, id):
    distributor = Distributor.objects.get(id=id)
    context ={'distributor': distributor}
    return render(request,'mainusers/distributor/view_distributor.html', context)

def update_distributor(request, id):
    distributor=get_object_or_404(Distributor, id=id)

    if request.method =='POST':
        form = DistributorUpdateForm(request.POST, instance=distributor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(view_distributor,  kwargs={'id':distributor.id  }))
    else:
        form = form = DistributorUpdateForm(instance=distributor)
        context={'form': form,
                'distributor': distributor,
            }
        return render(request,'mainusers/distributor/update_distributor.html', context)
