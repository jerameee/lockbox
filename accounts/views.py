from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# REGISTER VIEW
def register_view(request):
    """
    Handles user registration.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        HttpResponse: The rendered registration page or a redirect to the login page.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

# LOGIN VIEW
def login_view(request):
    """
    Handles user login.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        HttpResponse: The rendered login page or a redirect to the file list page.
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("file_list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# LOGOUT VIEW
def logout_view(request):
    """
    Handles user logout.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        HttpResponse: A redirect to the login page.
    """
    if request.method == "POST":
        logout(request)
        return redirect("login")
