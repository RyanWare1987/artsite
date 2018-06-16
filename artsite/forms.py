# Created this forms here due to not needing a whole app to handle just one contact form
from django import forms


class ContactForm(forms.Form):
    """
    The Contact Us form which is displayed on the Contact page
    We ask for the user's name, email and content, whilst
    the mobile number is optional as that is quite personal.
    """
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_number = forms.CharField()
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        """
        The self.fields here just rename the 
        titles of the fields we're asking the 
        user to fill in to make them a bit
        less formal.
        """
        self.fields['contact_name'].label = "Your Name:"
        self.fields['contact_email'].label = "Your Email:"
        self.fields['contact_number'].label = "Your Contact Number:"
        self.fields['content'].label = "Write your message to Ryan Ware here. Ask a question or enquire about a commission"