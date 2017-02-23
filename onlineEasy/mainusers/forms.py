from django.forms import ModelForm


from mainusers.models import Distributor

class DistributorCreateForm(ModelForm):
    class Meta:
        model = Distributor
        fields = ['name', 'short_code', 'contact', 'email', 'address1', 'address2','pin']


class DistributorUpdateForm(ModelForm):
    class Meta:
        model = Distributor
        fields = ['name', 'short_code', 'contact', 'email', 'address1', 'address2','pin']
