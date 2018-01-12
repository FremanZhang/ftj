from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name')


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    views = forms.IntegerField(max_length=256, initial=0)
    url = forms.CharField(max_length=256, help_text="Please enter the URL of the page.")

    class Meta:
        model = Page
        exclude = ('category')
        