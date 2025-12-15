from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, login_not_required
from .forms import UserForm, ProfileForm

@login_not_required
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('account:login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('account:login')
    return render(request, 'login.html')

@login_not_required
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirmpassword", "")
        if not all([username, email, password, confirm_password]):
            messages.error(request, "All fields are required.")
            return redirect('account:register')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('account:register')
        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return redirect('account:register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect('account:register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('account:register')
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Account created and logged in.")
                return redirect('home')
            messages.success(request, "Account created. Please login.")
            return redirect('account:login')
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
            return redirect('account:register')
    return render(request, 'login.html')

@login_required
def profile_page(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("account:profile")
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, "profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile": profile,
    })

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

