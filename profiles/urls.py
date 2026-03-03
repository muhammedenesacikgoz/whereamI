from django.urls import path
from .views import dashboard, profile_view, update_location, SignUpView, home_view, friends_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile/<str:username>/", profile_view, name="profile"),
    path("update-location/", update_location, name="update_location"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("home/", home_view, name="home"),
    path("friends/", friends_view, name="friends"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)