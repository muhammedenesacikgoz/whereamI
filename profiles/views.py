from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, User, Location
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    friends = Profile.objects.exclude(user=request.user)
    if request.method=="POST":
        loc_id = request.POST.get("location")

        if loc_id:
            profile.location = get_object_or_404(Location, id=loc_id)
            profile.save()

    locations = Location.objects.all()
    return render(request, "profiles/dashboard.html", {"profile": profile, "friends": friends, "locations": locations})

@login_required
def profile_view(request, username):
    user= get_object_or_404(User, username=username)
    profile = Profile.objects.get(user = user)
    my_profile = None
    if request.user.is_authenticated:
        my_profile= Profile.objects.get(user=request.user)
    friends = Profile.objects.exclude(user=request.user)
    context = {
        "profile": profile,
        "my_profile": my_profile,
        "friends": friends,
        "active_user": username,
        "locations": Location.objects.all(),

    }
    return render(request, "profiles/dashboard.html", context)
@login_required
def home_view(request):
    if request.method == "POST":
        pass
    return render(request, "home/home.html")

@login_required
def friends_view(request):
    if request.method == "POST":
        pass
    return render(request, "friends/friends.html")


@login_required
def update_location(request):
    if request.method == "POST":
        data = json.loads(request.body)
        loc_id = data.get("location")

        profile =request.user.profile
        profile.location_id = loc_id
        profile.save()

        return JsonResponse({"status": "ok"})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})


