from django.shortcuts import render

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
  return render(request, 'finches/index.html', {
    'finches': finches,
  })
    