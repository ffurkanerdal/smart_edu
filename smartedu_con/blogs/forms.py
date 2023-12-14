from django import forms
from .models import BlogComments

class CommentForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Your Comments"
    }))

    author  =   forms.CharField(widget=forms.HiddenInput)
    username    =   forms.CharField(widget=forms.HiddenInput)
    email   =   forms.CharField(widget=forms.HiddenInput)
    

    class Meta:
        model = BlogComments
        fields = ["message","author","username","email"]
