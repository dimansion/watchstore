from django.shortcuts import render, get_object_or_404
from .models import Men

def index(request):

    # Render the response and send it back!
    return render(request, 'watchstore/index.html')

def men(request):
    items = Men.objects.all()
    # Render the response and send it back!
    return render(request, 'watchstore/men.html', {'items': items})

def watch_detail(request, pk):
    post = get_object_or_404(Men, pk=pk)
    return render(request, 'watchstore/watch_detail.html', {'post': post})

