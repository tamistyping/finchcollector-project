from django.shortcuts import render
from .models import Finch

finches = [
  {'name': 'John', 'species': 'Zebra Finch', 'description': 'Cheerful and chirpy', 'age': 1},
  {'name': 'Mary', 'species': 'Gouldian Finch', 'description': 'Colorful and curious', 'age': 2},
  {'name': 'Jim', 'species': 'Society Finch', 'description': 'Social and playful', 'age': 1},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches,
  })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {'finch': finch})