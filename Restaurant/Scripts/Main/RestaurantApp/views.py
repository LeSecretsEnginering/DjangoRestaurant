from django.shortcuts import render
from .forms import MenuForm
from .models import Menu
# Create your views here.

def home(request):
    menu_images = Menu.objects.all()
    return render(request, 'home.html', {'menu_images': menu_images})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def category(request):
    category_items = Menu.objects.all()
    return render(request, 'category.html', {'category_items': category_items})

def menu_views(request):
   menu_items = Menu.objects.all()
   return render(request, 'menu.html', {'menu_items': menu_items})