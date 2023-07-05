from django import forms
from tinymce.widgets import TinyMCE

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    message = forms.CharField(widget=TinyMCE(), required=True,)
