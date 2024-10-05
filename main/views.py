from django.shortcuts import render, redirect
from .forms import WallpaperForm , Mobileform
from .models import Wallpaper , MobileWallpaper


def index(request):
  wallpapers = Wallpaper.objects.all().order_by('-upload_date')
  mwallpaper = MobileWallpaper.objects.all().order_by('-upload_date')
  return render(request, 'index.html',{'wallpapers': wallpapers , 
                                       'mwallpaper': mwallpaper})


# View for uploading wallpapers



def upload_wallpaper(request):
  if request.method == 'POST':
      form = WallpaperForm(request.POST, request.FILES )
      if form.is_valid():
          form.save()
          form = WallpaperForm()
          return redirect('upload')
  else:
      form = WallpaperForm()
  return render(request, 'upload.html', {'form': form})



def mobile_wallpaper(request):
  if request.method == 'POST':
      form = Mobileform(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        form = Mobileform()
        return redirect('mupload')
  else:
      form = Mobileform()
  return render(request, 'm_upload.html', {'form': form})





# Create your views here.
