from django.shortcuts import render
from .models import Men

def index(request):

    # Render the response and send it back!
    return render(request, 'watchstore/index.html')

def men(request):
    items = Men.objects.all()
    # Render the response and send it back!
    return render(request, 'watchstore/men.html', {'items': items})
