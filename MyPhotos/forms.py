__author__ = 'vijay'
from django import forms
from MyPhotos.models import AlbumPhoto

class PhotoUploadForm(forms.ModelForm):
    """Upload files with this form"""
    # def save(self, commit=True):
    #     instance = forms.ModelForm.save(self, commit=False)
    #     instance.filename = self.files['imageFile'].name
    #
    #     if commit:
    #         instance.save()
    #
    #     return instance
    class Meta:
        model = AlbumPhoto
        fields = ('imageFile','tags')