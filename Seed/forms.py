from django.forms import ModelForm
from django import forms
from .models import ImageUpload

class ImageExampleForm(ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']
        '''file = forms.CharField(
            label = "Image Upload"
            ,widget = forms.FileInput(
                            attrs=
                            {
                                'accept' : 'image/jpg,jpeg',
                                "class":"form-control",
                                "placeholder" : "Input Image",
                                "form" : "form-control"
                            }
                        )
                        )
'''
        #widgets = {'jpeg_file': forms.FileInput(attrs={'accept' : 'image/jpg,jpeg'}) }
