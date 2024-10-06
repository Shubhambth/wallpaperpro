from django.shortcuts import render, redirect
from .forms import WallpaperForm , Mobileform
from .models import Wallpaper , MobileWallpaper
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required







def index(request):
    wallpapers = Wallpaper.objects.all().order_by('-upload_date')
    mwallpaper = MobileWallpaper.objects.all().order_by('-upload_date')
    

    if request.method == 'GET':
        search_term = request.GET.get('search_term')
        if search_term:
            wallpapers = wallpapers.filter(title__icontains=search_term)
            mwallpaper = mwallpaper.filter(title__icontains=search_term)
            return render(request, 'index.html', {'wallpapers': wallpapers , 
                                'mwallpaper': mwallpaper})
    
    
            
    return render(request, 'index.html',{'wallpapers': wallpapers , 
                                       'mwallpaper': mwallpaper})


# View for uploading wallpapers


@login_required(login_url="login")
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


@login_required(login_url="login")
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



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'login.html')        


# Create your views here.
