from django import forms

from .models import MyModel


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        exclude = ("image_width", "image_height")
