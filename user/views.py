from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login
from user.forms import CustomUserCreateForm


def get_profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'user/profile.html')

def create_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
       form = CustomUserCreateForm(request.POST)
       if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user:profile")
    else:
        form = CustomUserCreateForm()

    return render(request, "user/create_user.html", {"form": form})