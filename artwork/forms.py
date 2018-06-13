from django import forms
from .models import OrderProduct

class MakePaymentForm(forms.Form):

    # Loop over Month and Year choices within the range parameters set.
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2040)]
    
    # Standard Stripe payment form inputs
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = (
            'full_name',
            'phone_number',
            'address_1',
            'address_2',
            'postcode',
            'city',
            'country'
        )