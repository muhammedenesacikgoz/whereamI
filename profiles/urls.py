from django.urls import path
from .views import dashboard, profile_view, update_location
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile/<str:username>/", profile_view, name="profile"),
    path("update-location/", update_location, name="update_location"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)