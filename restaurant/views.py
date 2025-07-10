from django.shortcuts import render
from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'restaurant/home.html')

def menu_list(request):
    items = Menu.objects.all()
    return render(request, 'restaurant/menu_list.html', {'menu': items})

def menu_detail(request, pk):
    item = Menu.objects.get(pk=pk)
    return render(request, 'restaurant/menu_detail.html', {'item': item})