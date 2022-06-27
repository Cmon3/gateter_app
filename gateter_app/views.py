from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from .models import Maullido, Profile
from .forms import MaullidoForm, CustomUserCreationForm

# Create your views here.


def dashboard(request):
    form = MaullidoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            maullido = form.save(commit=False)
            maullido.user = request.user
            maullido.save()
            return redirect("gateter_app:dashboard")

    followed_maullidos = Maullido.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(request, "gateter_app/dashboard.html", {"form": form, "maullidos": followed_maullidos})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect(reverse("gateter_app:dashboard"))
        messages.error(request, "El registro no se pudo completar.")
    else:
        form = CustomUserCreationForm()
    return render(
        request, "registration/register.html",
        {"form": form}
    )


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "gateter_app/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "gateter_app/profile.html", {"profile": profile})
