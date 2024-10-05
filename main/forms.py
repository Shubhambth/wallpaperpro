from django import forms
from .models import Wallpaper , MobileWallpaper

class WallpaperForm(forms.ModelForm):
    class Meta:
        model = Wallpaper
        fields = ['title', 'image']

class Mobileform(forms.ModelForm):
    class Meta:
        model = MobileWallpaper
        fields = ['title','image']