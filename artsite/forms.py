# Created this forms here due to not needing a whole app to handle just one contact form

from django import forms


#This is our contact form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_number = forms.CharField() #Not integer field because + chars
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        #Here we are just adding some labels to make the fields more friendly
        self.fields['contact_name'].label = "Your Name:"
        self.fields['contact_email'].label = "Your Email:"
        self.fields['contact_number'].label = "Your Contact Number:"
        self.fields['content'].label = "Write your message to Ryan Ware here. Ask a question or enquire about a commission"