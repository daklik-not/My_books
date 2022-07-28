from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from djbooks.models import Author, UsersLink
from django.contrib.auth.models import User

class PublisherForm(forms.Form):
    name = forms.CharField(label='Publisher name', max_length=30)
    address = forms.CharField(label='Publisher address', max_length=50)
    city = forms.CharField(label='Publisher city', max_length=60)
    country = forms.CharField(label='Publisher country', max_length=50)
    website = forms.URLField(label='Publisher website', max_length=100)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['salutation', 'name', 'email']

class UsersLinkForm(ModelForm):
    class Meta:
        model = UsersLink
        fields = ['url']

class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined']
