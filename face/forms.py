from django import forms
#from .models import Unknown


class OrderCreateForm(forms.ModelForm):
    class Meta:
        #model = Unknown
        fields = ['image']
    docfile = forms.FileField(
        label='image',
    )  

class UploadFileForm(forms.Form):
    file = forms.FileField()      