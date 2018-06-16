from django import forms
from .models import OrderProduct

class MakePaymentForm(forms.Form):

    """
    We loop over a range of choices to select from 
    drop down boxes within the options expiry_month
    and expiry_year
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2040)]
    
    """
    The parts of this form are for secure data to be input, 
    we do not save them against any user, or in the database as 
    they are completely handled by Stripe. 
    """
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """
    The OrderForm, which will meet the user with
    a form to enter the fields below - this will
    give us the information of where to send any
    product purchased by a user.
    """
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