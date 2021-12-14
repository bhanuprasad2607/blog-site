from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def loginPage(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back, to have great time!')
            return redirect('home')
        else:
            messages.add_message(
                request, 30, 'Login credentials are incorrect!', 'danger'
            )

    return render(request, 'user/login.html')


def logoutPage(request):
    logout(request)
    messages.info(request, 'You have logged out, See you soon! ')
    return redirect('home')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            return redirect('edit-account')

        else:
            messages.add_message(
                request, 30, 'An error has occurred during registration', 'danger')

    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)
