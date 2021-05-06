from django.shortcuts import render, reverse, redirect

# Create your views here.

def keci_home_view(request):
    context = {}
    return render(request, 'keci_home.html', context=context)

def new_project_view(request):
    context = {}
    return render(request, 'new_project.html', context=context)

def keci_search_view(request):
    context = {}
    return render(request, 'keci_search.html', context=context)

def keci_advanced_search_view(request):
    context = {}
    return render(request, 'keci_advanced_search.html', context=context)

def project_view(request):
    context = {}
    return render(request, 'project.html', context=context)

def help_view(request):
    context = {}
    return render(request, 'help.html', context=context)