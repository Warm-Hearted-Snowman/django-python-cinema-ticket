from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages import success, error
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginPage, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from ticket.models import Ticket


# Create your views here.
def is_not_authenticated(user):
    return not user.is_authenticated


@user_passes_test(is_not_authenticated, login_url='/account/')
def user_login(request):
    if request.method == 'POST':
        form = LoginPage(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movie:movies_list')
                else:
                    return render(request, 'disabled_account.html')  # Create a template for disabled accounts
            else:
                return render(request, 'invalid_login.html')  # Create a template for invalid login
    else:
        form = LoginPage()
        return render(request, 'registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def dashboard_info(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'userinfo.html', context)


@login_required
def dashboard_tickets(request):
    user = request.user
    context = {
        'user': user,
        'tickets': Ticket.objects.filter(user=user),
    }
    return render(request, 'user-tickets.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('movie:movies_list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])

            # Check if username already exists
            if Profile.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Username is already taken. Please choose a different one.')
                return render(request, 'account/register.html', {'user_form': form})

            new_user.save()
            login(request, new_user)
            messages.success(request, 'User created successfully.')
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            # Use messages framework to display form errors
            for field, error_messages in form.errors.items():
                for error_message in error_messages:
                    messages.error(request, error_message)

            return render(request, 'account/register.html', {'user_form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
