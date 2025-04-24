from django.shortcuts import render
def home(request):
    return render(request, 'index.html')
def template_selection(request):
    return render(request, 'template_selection.html')
