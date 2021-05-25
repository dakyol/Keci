from django.shortcuts import render, redirect

from accounts.forms import RegisterForm

# Create your views here.

def register_view(response):
    form = RegisterForm()
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('keci_home')
    context = {'form':form}

    return render(response, 'registration/register.html', context=context)