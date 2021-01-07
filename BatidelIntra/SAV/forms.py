from django import forms
from address.forms import AddressField


class SAVForm(forms.Form):
    address = AddressField()
