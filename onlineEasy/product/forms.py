from django.forms import ModelForm


from product.models import Product, PriceList

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'cost_price', 'discount_allowed']


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'cost_price', 'active','discount_allowed']
